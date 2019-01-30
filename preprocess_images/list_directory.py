
import os
class images_collections:
	paths = []
	def __init__(self,d_path):
		self.path=d_path
        #def load_png_images
	#def resize_images (target size, target dir)
	#def  get_features(directory for features)
	def get_list_files_directory(self, dir_path):
		paths=[]
		for root, dirs, files in os.walk(dir_path):
			for file in files:
    				if file.endswith(".dcm"):
					paths.append(os.path.join(root, file))
		return paths


#print get_list_files_directory("/home/ohje/Desktop/LIDC-IDRI/")
m = images_collections("/home/ohje/Desktop/LIDC-IDRI/")
print m.get_list_files_directory("/home/ohje/Desktop/LIDC-IDRI/")

