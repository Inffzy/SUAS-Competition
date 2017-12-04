from PIL import Image
from .color_operations import ColorOperations
from .blob_color_operations import BlobColorOperations

class FalsePositiveEliminator(object):

    @staticmethod
    def eliminate_overrepeated_colors(target_map_image, positive_list):
        """
        Eliminate false positives after blob detection.

        (This method works better when there are significantly more false
        positives than real targets)

        :param target_map_image: the image of the background
        :param positive_list: the list holding the information of the blobs.

        :type target_map_image: PIL image
        :type positive_list: a list of four-tuples containing four elements for each
                             blob: (x, y, length, width)
        :type x: int
        :type y: int
        :type length: int
        :type width: int

        Concept:
        Find the average color of all the blobs. Compare that color to the color
        of each blob. Save all the blobs with colors that stand out from the
        rest and eliminate the rest. The colors of the targets differ from the
        colors of the background. By eliminating the blobs of the background,
        targets remain.
        """
        blob_color_list = []
        for index in range(len(positive_list)):
            average_blob_color = BlobColorOperations.find_blob_average_color(target_map_image, positive_list[index])
            blob_color_list.append(average_blob_color)

        average_list_color_x = 0
        average_list_color_y = 0
        average_list_color_z = 0

        for index in range(len(blob_color_list)):
            average_list_color_x += blob_color_list[index][0]
            average_list_color_y += blob_color_list[index][1]
            average_list_color_z += blob_color_list[index][2]

        average_list_color = (average_list_color_x / len(blob_color_list) , average_list_color_y / len(blob_color_list), average_list_color_z / len(blob_color_list))

        remaining_blob_list = []
        index = len(positive_list) - 1
        while (index >= 0):
            percentage_difference = ColorOperations.find_percentage_difference(average_list_color, blob_color_list[index])

            if (percentage_difference >= 15):
                remaining_blob_list.append(positive_list[index])

            index -= 1

        return remaining_blob_list

    @staticmethod
    def eliminate_by_surrounding_color(target_map_image, positive_list):
        """
        Eliminate false positives after blob detection.

        (This method works better when there are less number of false positives.
        If this condition does not apply, use eliminate_overrepeated_colors
        first to ensure better results.)

        :param target_map_image: the image of the background
        :param positive_list: the list holding the information of the blobs.

        :type target_map_image: PIL image
        :type positive_list: a list of four-tuples containing four elements for each
                             blob: (x, y, length, width)
        :type x: int
        :type y: int
        :type length: int
        :type width: int

        Concept:
        For every blob given by positive_list, if its surrounding color is below
        a certain threshold, eliminate this blob. The targets have colors that
        stand out from the background, if a blob's color conforms with the
        background color, then it is not a target.
        """
        list_to_eliminate = []
        for index in range(len(positive_list)):
            average_surrounding_color = BlobColorOperations.find_surrounding_average_color(target_map_image, positive_list[index])
            average_blob_color = BlobColorOperations.find_blob_average_color(target_map_image, positive_list[index])

            percentage_difference = ColorOperations.find_percentage_difference(average_surrounding_color, average_blob_color)
            if (percentage_difference <= 10):
                list_to_eliminate.append(index)

        list_to_eliminate = list(set(list_to_eliminate))
        list_to_eliminate.sort()

        index = len(list_to_eliminate) - 1
        while (index >= 0):
            positive_list.pop(list_to_eliminate[index])
            index -= 1

        return positive_list

    @staticmethod
    def eliminate_close_by_targets(positive_list):
        """
        :param target_map_image: the image of the background
        :param positive_list: the list holding the information of the blobs.

        :type target_map_image: PIL image
        :type positive_list: a list of four-tuples containing four elements for each
                             blob: (x, y, length, width)
        :type x: int
        :type y: int
        :type length: int
        :type width: int
        """
        close_by_targets = []
        list_to_append = []
        list_to_eliminate = []

        for index_1 in range(len(positive_list)):
            for index_2 in range(index_1 + 1, len(positive_list)):

                if ((positive_list[index_1] == -1) or (positive_list[index_2] == -1)):
                    continue

                target_1_center_x = positive_list[index_1][0] + (positive_list[index_1][2] / 2)
                target_1_center_y = positive_list[index_1][1] + (positive_list[index_1][3] / 2)
                target_2_center_x = positive_list[index_2][0] + (positive_list[index_2][2] / 2)
                target_2_center_y = positive_list[index_2][1] + (positive_list[index_2][3] / 2)

                x_distance = abs(target_1_center_x - target_2_center_x)
                y_distance = abs(target_1_center_y - target_2_center_y)

                target_1_radius = positive_list[index_1][2]
                target_2_radius = positive_list[index_2][2]

                if ((x_distance < ((target_1_radius + target_2_radius) * 1.5)) and (y_distance < ((target_1_radius + target_2_radius) * 1.5))):
                    close_by_targets.append([positive_list[index_1], positive_list[index_2]])
                    positive_list[index_1] = -1
                    positive_list[index_2] = -1

        for index in range(len(close_by_targets)):
            target_1_x = close_by_targets[index][0][0]
            target_1_y = close_by_targets[index][0][1]
            target_1_width = close_by_targets[index][0][2]
            target_1_height = close_by_targets[index][0][3]

            target_2_x = close_by_targets[index][1][0]
            target_2_y = close_by_targets[index][1][1]
            target_2_width = close_by_targets[index][1][2]
            target_2_height = close_by_targets[index][1][3]

            average_x = (target_1_x + target_2_x) / 2
            average_y = (target_1_y + target_2_y) / 2
            average_width = (target_1_width + target_2_width) / 2
            average_height = (target_1_height + target_2_height) / 2

            list_to_append.append((average_x, average_y, average_width, average_height))

        index = len(positive_list) - 1
        while (index >= 0):
            if (positive_list[index] == -1):
                positive_list.pop(index)
            index -= 1

        for index in range(len(list_to_append)):
            positive_list.append(list_to_append[index])

        number_of_close_by_targets = len(close_by_targets)

        return [positive_list, number_of_close_by_targets]
