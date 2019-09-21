from fastai.vision import *


torch.cuda.set_device(0)

PATH = "/home/weilun/Documents/Proj/data/"


tfms = get_transforms()
data = ImageDataBunch.from_folder(PATH, ds_tfms=tfms, bs=64, size=256)

learn = cnn_learner(data, models.resnet34, metrics=accuracy)

learn.fit_one_cycle(30)

# img = open_image(
#     '/home/weilun/Documents/Proj/data/valid/Bhuiya Hasan/imageOut 23.jpg')
# learn.predict(img)

learn.save('trained model', return_path=True)
learn = learn.load("trained model")

preds, y, losses = learn.get_preds(with_loss=True)
interp = ClassificationInterpretation(learn, preds, y, losses)
interp.plot_top_losses(4, figsize=(7, 7))
interp.most_confused()
