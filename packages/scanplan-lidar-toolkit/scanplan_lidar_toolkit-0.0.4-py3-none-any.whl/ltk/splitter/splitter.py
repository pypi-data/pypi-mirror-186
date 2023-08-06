from ..azure import BlobService
import numpy
import laspy
import io

class Splitter (object):
    
    def __init__(self):
        self.blob_service = BlobService()

    def read_las(self, las_url: str):
        
        las_bytes = self.blob_service.download_blob(las_url)
        return laspy.read(las_bytes)


    def split(self, lasdata, n=int(2e5)) -> list:
        splits = []
        las_cnt = len(lasdata)
        if las_cnt < n:
            splits.append(lasdata)
        else:
            num_splits = numpy.ceil(las_cnt / n).astype(int)
            lc = 0  # low capacity
            for i in range(1, num_splits+1):
                uc = int(n*i)
                if uc > las_cnt:
                    uc = las_cnt
                las_split = lasdata[lc:uc]
                splits.append(las_split)
                lc = uc
        return splits


    def write_splits(self, splits: list, splitted_url: str, folder: str):
        
        uploaded_files = []
        
        for i, s in enumerate(splits):
            points = numpy.vstack((s.x, s.y, s.z)).transpose()
            
            blob_to_store = io.BytesIO()
            numpy.save(blob_to_store, points)
            
            blob_name = f'{splitted_url}/{folder}/split_{str(i)}.npy'
            self.blob_service.upload_blob(blob_name, blob_to_store)
            
            uploaded_files.append(blob_name)

        return uploaded_files