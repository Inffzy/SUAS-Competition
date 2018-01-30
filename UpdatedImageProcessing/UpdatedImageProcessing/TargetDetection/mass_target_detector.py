<<<<<<< HEAD
import os
from .settings import Settings
from .logger import Logger
from .result_recorder import ResultRecorder
from .integrated_target_detection_process import IntegratedTargetDetectionProcess
from .integrated_target_capturing_process import IntegratedTargetCapturingProcess

class MassTargetDetector(object):

    @staticmethod
    def detect_mass_target(path_to_target_maps_folder):
        list_of_crops = []
        list_of_json_files = []
        number_of_target_maps = len(os.listdir(path_to_target_maps_folder))

        for index_1 in range(1, number_of_target_maps + 1):
            current_target_map = os.path.join(path_to_target_maps_folder, str(index_1) + ".jpg")

            positive_list = IntegratedTargetDetectionProcess.run_integrated_target_detection_process(current_target_map)
            capturing_results = IntegratedTargetCapturingProcess.run_integrated_target_capturing_process(current_target_map, positive_list)
            single_target_crops = capturing_results[0]
            list_to_eliminate = capturing_results[1]

            index_2 = len(list_to_eliminate) - 1
            while(index_2 >= 0):
                positive_list.pop(list_to_eliminate[index_2])
                index_2 -= 1

            json_file = ResultRecorder.record_result(positive_list)

            list_of_crops.append(single_target_crops)
            list_of_json_files.append(json_file)

            Logger.log("Detection for Target Map " + str(index_1) + " Completed")

        return [list_of_crops, list_of_json_files]
||||||| merged common ancestors
=======
import os
from .settings import Settings
from .logger import Logger
from .result_recorder import ResultRecorder
from .integrated_target_detection_process import IntegratedTargetDetectionProcess
from .integrated_target_capturing_process import IntegratedTargetCapturingProcess

class MassTargetDetector(object):

    @staticmethod
    def detect_mass_target(path_to_target_maps_folder):
        list_of_crops = []
        list_of_json_files = []
        number_of_target_maps = len(os.listdir(path_to_target_maps_folder))

        for index_1 in range(1, number_of_target_maps + 1):
            current_target_map = os.path.join(path_to_target_maps_folder, str(index_1) + ".jpg")

            positive_list = IntegratedTargetDetectionProcess.run_integrated_target_detection_process(current_target_map)
            capturing_results = IntegratedTargetCapturingProcess.run_integrated_target_capturing_process(current_target_map, positive_list)
            single_target_crops = capturing_results[0]
            list_to_eliminate = capturing_results[1]

            index_2 = len(list_to_eliminate) - 1
            while(index_2 >= 0):
                positive_list.pop(list_to_eliminate[index_2])
                index_2 -= 1

            json_file = ResultRecorder.record_result(positive_list)

            list_of_crops.append(single_target_crops)
            list_of_json_files.append(json_file)

            Logger.log("Detection for Target Map " + str(index_1) + " Completed")

        return [list_of_crops, list_of_json_files]
<<<<<<< HEAD



#The following lines for multiprocessing are still under developments.
'''
import os, multiprocessing, timeit
from .target_detection_settings import TargetDetectionSettings
from .target_detection_logger import TargetDetectionLogger
from .blob_detector import BlobDetector
from .target_detector import TargetDetector
from .false_positive_eliminator import FalsePositiveEliminator
from .automatic_tester import AutomaticTester

def run_target_detector(target_map_answer_index_combo_list):
    current_target_map = target_map_answer_index_combo_list[0]
    current_target_map_answer = target_map_answer_index_combo_list[1]
    index_number = target_map_answer_index_combo_list[2]

    positive_list = TargetDetector.detect_targets(current_target_map)

    single_target_capturer_results = SingleTargetsCapturer.capture_single_targets(current_target_map, positive_list)
    single_target_crops = single_target_capturer_results[0]
    list_to_eliminate = single_target_capturer_results[1]

    for index_2 in range(len(single_target_crops)):
        single_target_crops[index_2].save(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops", str(index) + "-" + str(index_2 + 1) + ".png"))

    index_3 = len(list_to_eliminate) - 1
    while(index_3 >= 0):
        positive_list.pop(list_to_eliminate[index_3])
        index_3 -= 1

    combo_positive_list = AutomaticTester.run_automatic_tester(positive_list, current_target_map_answer)
    true_positive_list = combo_positive_list[0]
    false_positive_list = combo_positive_list[1]
    AutomaticTester.save_result(true_positive_list, false_positive_list, index_number)

    TargetDetectionLogger.log("Detection for Target Map " + str(index_number) + " Completed")

class MassTargetDetector(object):

    @staticmethod
    def detect_mass_target():
        if (os.path.isdir(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH)):
            raise Exception("Cannot create Target_Detection_Report: Save directory already exists")
        os.mkdir(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH)

        if (os.path.isdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Target_Map_Reports"))):
            raise Exception("Cannot create Target_Map_Reports: Save directory already exists")
        os.mkdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Target_Map_Reports"))

        if (os.path.isdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops"))):
            raise Exception("Cannot create Single_Target_Crops: Save directory already exists")
        os.mkdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops"))

        target_map_answer_index_combo_list = []

        for index in range(1, TargetDetectionSettings.NUMBER_OF_TARGET_MAPS + 1):
            current_target_map = os.path.join(TargetDetectionSettings.TARGET_MAPS_PATH, str(index) + ".jpg")
            current_target_map_answer = os.path.join(TargetDetectionSettings.TARGET_MAPS_ANSWERS_PATH, str(index) + ".json")

            target_map_answer_index_combo_list.append([current_target_map, current_target_map_answer, index])

        pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())
        maps_per_process = TargetDetectionSettings.NUMBER_OF_TARGET_MAPS / multiprocessing.cpu_count()

        AutomaticTester.report_result()
'''

'''
    @staticmethod
    def run_mass_target_detector(maps_per_process, process_number):
        for index in range(1, maps_per_process + 1):
            current_target_map = TargetDetectionSettings.TARGET_MAPS_PATH + "/" + str(index + process_number) + ".jpg"
            current_target_map_answers = TargetDetectionSettings.TARGET_MAPS_ANSWERS_PATH + "/" + str(index + process_number) + ".json"

            positive_list = BlobDetector(current_target_map).detect_blobs()

            if (len(positive_list) > 15):
                positive_list = FalsePositiveEliminator.eliminate_overrepeated_colors(current_target_map, positive_list)

            positive_list = FalsePositiveEliminator.eliminate_overlapping_blobs(positive_list)
            positive_list = FalsePositiveEliminator.eliminate_by_surrounding_color(current_target_map, positive_list)
            print positive_list
            #return AutomaticTester(positive_list, current_target_map_answers).run_automatic_tester()

    #standard multiprocessing
    @staticmethod
    def detect_mass_target():
        cpu_count = multiprocessing.cpu_count()
        maps_per_process = (TargetDetectionSettings.NUMBER_OF_TARGET_MAPS / cpu_count)
        start_time = timeit.default_timer()

        jobs = []
        for index in range(cpu_count):
            starting_index = index * int(maps_per_process)
            target_detection_process = multiprocessing.Process(target=MassTargetDetector.run_mass_target_detector, args=(maps_per_process, starting_index))
            jobs.append(target_detection_process)
            target_detection_process.start()

        for job in jobs:
            job.join()

        TargetDetectionLogger.log("Target Detection Results saved at: " + TargetDetectionSettings.TARGET_DETECTION_SAVE_PATH)

        print("====================================")
        print("Total number of target_maps detected:", len(os.listdir(TargetDetectionSettings.TARGET_DETECTION_SAVE_PATH)))
        print("Total elapsed time (sec):", timeit.default_timer() - start_time)
        print("====================================")
'''
>>>>>>> Separated the detection process from the testing process to prepare for the integration
||||||| merged common ancestors



#The following lines for multiprocessing are still under developments.
'''
import os, multiprocessing, timeit
from .target_detection_settings import TargetDetectionSettings
from .target_detection_logger import TargetDetectionLogger
from .blob_detector import BlobDetector
from .target_detector import TargetDetector
from .false_positive_eliminator import FalsePositiveEliminator
from .automatic_tester import AutomaticTester

def run_target_detector(target_map_answer_index_combo_list):
    current_target_map = target_map_answer_index_combo_list[0]
    current_target_map_answer = target_map_answer_index_combo_list[1]
    index_number = target_map_answer_index_combo_list[2]

    positive_list = TargetDetector.detect_targets(current_target_map)

    single_target_capturer_results = SingleTargetsCapturer.capture_single_targets(current_target_map, positive_list)
    single_target_crops = single_target_capturer_results[0]
    list_to_eliminate = single_target_capturer_results[1]

    for index_2 in range(len(single_target_crops)):
        single_target_crops[index_2].save(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops", str(index) + "-" + str(index_2 + 1) + ".png"))

    index_3 = len(list_to_eliminate) - 1
    while(index_3 >= 0):
        positive_list.pop(list_to_eliminate[index_3])
        index_3 -= 1

    combo_positive_list = AutomaticTester.run_automatic_tester(positive_list, current_target_map_answer)
    true_positive_list = combo_positive_list[0]
    false_positive_list = combo_positive_list[1]
    AutomaticTester.save_result(true_positive_list, false_positive_list, index_number)

    TargetDetectionLogger.log("Detection for Target Map " + str(index_number) + " Completed")

class MassTargetDetector(object):

    @staticmethod
    def detect_mass_target():
        if (os.path.isdir(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH)):
            raise Exception("Cannot create Target_Detection_Report: Save directory already exists")
        os.mkdir(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH)

        if (os.path.isdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Target_Map_Reports"))):
            raise Exception("Cannot create Target_Map_Reports: Save directory already exists")
        os.mkdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Target_Map_Reports"))

        if (os.path.isdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops"))):
            raise Exception("Cannot create Single_Target_Crops: Save directory already exists")
        os.mkdir(os.path.join(TargetDetectionSettings.TARGET_DETECTION_REPORT_SAVE_PATH, "Single_Target_Crops"))

        target_map_answer_index_combo_list = []

        for index in range(1, TargetDetectionSettings.NUMBER_OF_TARGET_MAPS + 1):
            current_target_map = os.path.join(TargetDetectionSettings.TARGET_MAPS_PATH, str(index) + ".jpg")
            current_target_map_answer = os.path.join(TargetDetectionSettings.TARGET_MAPS_ANSWERS_PATH, str(index) + ".json")

            target_map_answer_index_combo_list.append([current_target_map, current_target_map_answer, index])

        pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())
        maps_per_process = TargetDetectionSettings.NUMBER_OF_TARGET_MAPS / multiprocessing.cpu_count()

        AutomaticTester.report_result()
'''

'''
    @staticmethod
    def run_mass_target_detector(maps_per_process, process_number):
        for index in range(1, maps_per_process + 1):
            current_target_map = TargetDetectionSettings.TARGET_MAPS_PATH + "/" + str(index + process_number) + ".jpg"
            current_target_map_answers = TargetDetectionSettings.TARGET_MAPS_ANSWERS_PATH + "/" + str(index + process_number) + ".json"

            positive_list = BlobDetector(current_target_map).detect_blobs()

            if (len(positive_list) > 15):
                positive_list = FalsePositiveEliminator.eliminate_overrepeated_colors(current_target_map, positive_list)

            positive_list = FalsePositiveEliminator.eliminate_overlapping_blobs(positive_list)
            positive_list = FalsePositiveEliminator.eliminate_by_surrounding_color(current_target_map, positive_list)
            print positive_list
            #return AutomaticTester(positive_list, current_target_map_answers).run_automatic_tester()

    #standard multiprocessing
    @staticmethod
    def detect_mass_target():
        cpu_count = multiprocessing.cpu_count()
        maps_per_process = (TargetDetectionSettings.NUMBER_OF_TARGET_MAPS / cpu_count)
        start_time = timeit.default_timer()

        jobs = []
        for index in range(cpu_count):
            starting_index = index * int(maps_per_process)
            target_detection_process = multiprocessing.Process(target=MassTargetDetector.run_mass_target_detector, args=(maps_per_process, starting_index))
            jobs.append(target_detection_process)
            target_detection_process.start()

        for job in jobs:
            job.join()

        TargetDetectionLogger.log("Target Detection Results saved at: " + TargetDetectionSettings.TARGET_DETECTION_SAVE_PATH)

        print("====================================")
        print("Total number of target_maps detected:", len(os.listdir(TargetDetectionSettings.TARGET_DETECTION_SAVE_PATH)))
        print("Total elapsed time (sec):", timeit.default_timer() - start_time)
        print("====================================")
'''
=======
>>>>>>> Cleaned up some code in Image Processing
