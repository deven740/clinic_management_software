import torchvision.transforms as transforms
from PIL import Image
import io

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    print('image.size', image.size)
    im = my_transforms(image)
    print('im.shape',im.shape)
    print('im unsqueeze',im.unsqueeze(0).shape)
    return im.unsqueeze(0)


def predict(image_bytes):
    print('in predict')
    transform_image(image_bytes=image_bytes)