"""
helper functions for torch.

installing pytorch:
    pip install torch
    pip install torchvision


implementation ref.:
    Dataset, Dataloader
    https://pytorch.org/tutorials/beginner/basics/data_tutorial.html

    read_image(): return Tensor
    https://pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image


    transform, target_transform
    https://pytorch.org/tutorials/beginner/basics/transforms_tutorial.html

    from torchvision.transforms import ToTensor, Lambda

    ds = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor(),
        target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
    )


"""
import dataset as neudataset # neuralworks dataset class

import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
from torchvision.io import read_image
from PIL import Image

#######################################################
##### torch Dataset for CLASSIFICATION
"""
Creating a Custom Dataset for your files
A custom Dataset class must implement three functions: __init__, __len__, and __getitem__. 
"""
class ClassificationDatasetFromNeuDataset(Dataset):
    def __init__(self, image_path_list, label_index_list, transform=None, target_transform=None):
        """_summary_

        Args:
            img_file_list (_type_): _description_
            label_index_list (_type_): _description_
            transform (_type_, optional): _description_. Defaults to None.
            target_transform (_type_, optional): _description_. Defaults to None.
        """
        self.image_path_list = image_path_list
        self.label_index_list = label_index_list
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        try:
            return len(self.image_path_list)
        except:
            return 0

    def __getitem__(self, idx):
        """_summary_

        Args:
            idx (_type_): _description_

        Raises:
            IndexError: _description_

        Returns:
            _type_: tuple of (Tensor, Int) == (image Tensor, label index)
        """
        if idx >= len(self):
            raise IndexError

        img_path = self.image_path_list[idx]
        label_index = self.label_index_list[idx]
        pil_img = Image.open(img_path) # PIL image
        width, height = pil_img.size # pil_img.size == tuple of (width, height)
        if self.transform:
            image = self.transform(pil_img)
        else:
            image = ToTensor(pil_img)
            
        if self.target_transform:
           label_index = self.target_transform(label_index)

        return image, label_index


#######################################################
##### torch Dataset for Detectoion
class DetectionDatasetFromNeuDataset(Dataset):
    def __init__(self, image_path_list, bbox_list, transform=None, target_transform=None):
        """_summary_

        Args:
            img_file_list (_type_): _description_
            bbox_list (_type_): _description_
            transform (_type_, optional): _description_. Defaults to None.
            target_transform (_type_, optional): _description_. Defaults to None.
        """
        self.image_path_list = image_path_list
        self.bbox_list = bbox_list
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        try:
            return len(self.image_path_list)
        except:
            return 0

    def __getitem__(self, idx):
        """_summary_

        Args:
            idx (_type_): _description_

        Raises:
            IndexError: _description_

        Returns:
            _type_: tuple of (Tensor of image data, Tensor of 5 float values) == (image Tensor, bbox info)
        """
        if idx >= len(self):
            raise IndexError

        img_path = self.image_path_list[idx]
        label_index = self.label_index_list[idx]
        pil_img = Image.open(img_path) # PIL image
        if self.transform:
            image = self.transform(pil_img)
        else:
            image = ToTensor(pil_img)
            
        bbox = self.bbox_list[idx] # bbox == (label_index, center_x, center_y, width, height)
        torch_bbox = torch.FloatTensor(bbox)
                    
        if self.target_transform:
           torch_bbox = self.target_transform(torch_bbox)

        return image, torch_bbox
        

#####
class TorchDatasetGetter:
    def __init__(self, neuds, transform=None, target_transform=None, resize_spec=None, bbox_format=None) -> None:
        """_summary_

        Args:
            neuds (_type_): _description_
            transform (_type_, optional): _description_. Defaults to None.
            target_transform (_type_, optional): _description_. Defaults to None.
            resize_spec (_type_, optional): tuple. (width, height) of the resized image. Defaults to None.
        """
        self.neuds = neuds
        self.problem_type = getattr(neuds, "problem_type", "UNKNOWN")
        self.transform = transform
        self.target_transform = target_transform
        self.resize_spec = resize_spec
        pass
    
    def get_dataset(self, forwhat="train"):
        if forwhat == "train":
            data = self.neuds.train_data()
        elif forwhat == "validation":
            data = self.neuds.valid_data()
        elif forwhat == "test":
            data = self.neuds.test_data()
        else:
            raise ValueError(f"torch helper.py - TorchDatasetGetter class - get_dataset(): forwhat value [{forwhat}] is WRONG")                            
        
        ##
        if self.problem_type == "CLASSIFICATION":
            image_path_list = data[0]
            label_name_list = data[1]
            label_index_list = [self.neuds.get_label_index(name) for name in label_name_list]
            
            torchds = ClassificationDatasetFromNeuDataset(
                image_path_list,
                label_index_list,
                transform=self.transform, 
                target_transform=self.target_transform
            )
        
        ##    
        elif self.problem_type == "DETECTION":
            
            image_path_list = data[0]
            bbox_list = data[1] # tuple (label_index, center_x, center_y, width, height)
            
            torchds = DetectionDatasetFromNeuDataset(
                image_path_list,
                bbox_list,
                transform=self.transform, 
                target_transform=self.target_transform
            )
            
        else:
            raise ValueError(f"torch helper.py - TorchDatasetGetter class - get_dataset() problem_type={self.problem_type} is invalid.")
        
        return torchds
    
    
#############################        
if __name__ == "__main__":
    neuds  = None
    getter = TorchDatasetGetter(neuds)
    ds = getter.get_dataset(forwhat="train")
    pass