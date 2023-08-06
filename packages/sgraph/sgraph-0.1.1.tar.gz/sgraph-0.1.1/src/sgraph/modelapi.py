import functools

from sgraph import SElement
from sgraph import SElementAssociation
from sgraph import SGraph


class ModelApi:
    def __init__(self, filepath=None, model=None):
        if filepath:
            self.model = SGraph.parse_xml(filepath)
        elif model:
            self.model = model

        self.egm = model

    def getElementByPath(self, filepath):
        return self.egm.getElementFromPath(filepath)

    def getChildrenByType(self, element, elemType):
        return [x for x in element.children if x.typeEquals(elemType)]

    def getElementsByName(self, name):
        matching = list()

        def recursiveTraverser(elem):
            if elem.name == name:
                matching.append(elem)
            for child in elem.children:
                recursiveTraverser(child)

        recursiveTraverser(self.egm.rootNode)
        return matching

    def getCalledFunctions(self, funcElem):
        functionCalls = [x for x in funcElem.outgoing if x.deptype == 'function_ref']
        return set(map(lambda x: x.toElement, functionCalls))

    def getCallingFunctions(self, funcElem):
        functionCalls = [x for x in funcElem.incoming if x.deptype == 'function_ref']
        return set(map(lambda x: x.fromElement, functionCalls))

    def getUsedElements(self, elem):
        associations = [x for x in elem.outgoing]
        return set(map(lambda x: x.fromElement, associations))

    def getUserElements(self, elem):
        associations = [x for x in elem.incoming]
        return set(map(lambda x: x.fromElement, associations))

    def filter(self, filterfunc):
        matched_elements = []
        for c in self.egm.rootNode.children:
            self.__filter(c, filterfunc, matched_elements)
        return matched_elements

    def __filter(self, c, filterfunc, matched_elements):
        if filterfunc(c):
            matched_elements.append(c)
        for cc in c.children:
            self.__filter(cc, filterfunc, matched_elements)

    def query_dependencies_between(self, from_elems, to_elems, dep_filter, prevent_self_deps):
        found = []
        for f in from_elems:
            s = list()
            s.append(f)
            while len(s) > 0:
                elem = s.pop()
                if elem.outgoing is not None:
                    for ea in elem.outgoing:
                        if prevent_self_deps and self.matches_with_descendant(ea.toElement,
                                                                              tuple([f])):
                            pass
                        elif ea.toElement in to_elems or self.matches_with_descendant(
                                ea.toElement, tuple(to_elems)):
                            self.add_if_matches(ea, found, dep_filter)

                for c in elem.children:
                    s.append(c)
        return found

    def query_dependencies(self, elements, exclude, dep_filter, direction_is_out,
                           prevent_self_deps):
        found = []
        for f in elements:
            s = list()
            s.append(f)
            while len(s) > 0:
                elem = s.pop()
                if direction_is_out:
                    relations = elem.outgoing
                else:
                    relations = elem.incoming
                if relations is not None:
                    for ea in relations:
                        if direction_is_out:
                            other_elem = ea.toElement
                        else:
                            other_elem = ea.fromElement

                        if exclude is None:
                            if not ModelApi.intra_file(ea):
                                found.append(ea)

                        elif prevent_self_deps and self.matches_with_descendant(other_elem,
                                                                                tuple([f])):
                            pass

                        elif other_elem not in exclude and not self.matches_with_descendant(
                                other_elem, tuple(exclude)):
                            self.add_if_matches(ea, found, dep_filter)

                for c in elem.children:
                    s.append(c)
        return found

    @functools.lru_cache(maxsize=None)
    def matches_with_descendant(self, elem: SElement, potential_ancestors_list):
        # NOTE: LRU CACHE NEEDS TO BE CLEARED IF THE MODEL IS CHANGED!
        for potential_ancestor in potential_ancestors_list:
            if elem.isDescendantOf(potential_ancestor):
                return True
        return False

    @staticmethod
    def intra_file(ea):
        return ea.fromElement.getAncestorOfType('file') == ea.toElement.getAncestorOfType('file')

    @staticmethod
    def not_a_sibling_ref(ea):
        if ea.fromElement.parent == ea.toElement.parent:
            return False
        return True

    def add_if_matches(self, ea, found, dep_filter):
        if dep_filter is not None:
            if dep_filter[1] == '==' and ea.check_attr(dep_filter[0], dep_filter[2]):
                if not ModelApi.intra_file(ea):
                    found.append(ea)
            elif dep_filter[1] == '!=' and not ea.check_attr(dep_filter[0], dep_filter[2]):
                if not ModelApi.intra_file(ea):
                    found.append(ea)
            elif dep_filter[1] == 'in' and dep_filter[2] in ea.attrs.get(dep_filter[0], ''):
                if not ModelApi.intra_file(ea):
                    found.append(ea)
        else:
            if not ModelApi.intra_file(ea):
                found.append(ea)

    def filter_model(self, source_elem, source_graph):
        sub_graph = SGraph()
        sub_graph.createOrGetElement(source_elem)
        stack = [source_elem]
        # Traverse related elements from the source_graph using stack
        while stack:
            elem = stack.pop(0)
            new_elem = sub_graph.createOrGetElement(elem)
            new_elem.attrs = elem.attrs
            for ea in elem.outgoing:
                selem_from = new_elem
                to_element = ea.toElement
                selem_to = sub_graph.createOrGetElement(to_element)
                sea = SElementAssociation(selem_from, selem_to, ea.deptype, ea.attrs)
                sea.initElems()
                if len(to_element.children) > 0:
                    for child in to_element.children:
                        sub_graph.createOrGetElement(child)
            for ea in elem.incoming:
                selem_from = sub_graph.createOrGetElement(ea.fromElement)
                selem_to = new_elem
                sea = SElementAssociation(selem_from, selem_to, ea.deptype, ea.attrs)
                sea.initElems()
            stack.extend(elem.children)

        # Now that elements have been created, copy attribute data from the whole graph, via
        # traversal using two stacks.
        stack = [sub_graph.rootNode]
        whole_graph_stack = [source_graph.rootNode]
        while stack:
            elem = stack.pop(0)
            corresponding_source_elem = whole_graph_stack.pop(0)
            elem.attrs = corresponding_source_elem.attrs.copy()
            for elem in elem.children:
                stack.append(elem)
                whole_graph_stack.append(corresponding_source_elem.getChildByName(elem.name))

        return sub_graph
