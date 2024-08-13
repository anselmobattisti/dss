class helper:

    @staticmethod
    def create_link_splitting_map(n_vnfs: int):
        """
        Cria um mapa de divisão de links para uma quantidade dada de VNFs.

        Args:
            n_vnfs (int): Número de VNFs na cadeia de funções de serviço.

        Returns:
            list: Lista de arrays booleanos indicando onde as divisões ocorrem.
        """
        valid_plan_num = 2 ** (n_vnfs - 1)
        array_length = n_vnfs - 1  # Porque temos n-1 possíveis divisões entre n VNFs
        links_to_segment = []

        for i in range(valid_plan_num):
            bin_rep = format(i, f'0{array_length}b')
            boolean_array = [char == '1' for char in bin_rep]
            links_to_segment.append(boolean_array)

        return links_to_segment

    @staticmethod
    def create_segmentation_plans(vnfs, links_to_segment):
        """
        Cria planos de segmentação para uma lista de VNFs com base no mapa de divisão de links.

        Args:
            vnfs (list): Lista de VNFs na cadeia de funções de serviço.
            links_to_segment (list): Mapa de divisões dos links (lista de booleanos).

        Returns:
            list: Lista de planos de segmentação, onde cada plano é uma lista de segmentos.
        """
        segmentation_plan = []
        i = 0
        while i < len(vnfs):
            segment = [vnfs[i]]
            current_index = i
            for j in range(i, len(links_to_segment)):
                if links_to_segment[j]:
                    break
                if j + 1 < len(vnfs):
                    segment.append(vnfs[j + 1])
                    current_index = j + 1
            i = current_index + 1
            segmentation_plan.append(segment)

        return segmentation_plan

    @staticmethod
    def generate_all_segmentation_plans(vnfs):
        """
        Gera todos os planos de segmentação possíveis para uma lista de VNFs.

        Args:
            vnfs (list): Lista de VNFs na cadeia de funções de serviço.

        Returns:
            list: Lista de todos os planos de segmentação possíveis.
        """
        all_segmentation_plans = []
        links_to_segment = helper.create_link_splitting_map(len(vnfs))

        for split_map in links_to_segment:
            segmentation_plan = helper.create_segmentation_plans(vnfs, split_map)
            all_segmentation_plans.append(segmentation_plan)

        return all_segmentation_plans