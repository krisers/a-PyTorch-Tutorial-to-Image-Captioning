from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/home/kriselda/source/Datasets/coco/annotations/dataset_coco.json',
                       image_folder='/home/kriselda/source/Datasets/coco/images',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/home/kriselda/source/Datasets/coco/images',
                       max_len=50)
