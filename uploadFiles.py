from dropbox import dropbox

class TransferData:
    def __init__(self , access_token):
        self.access_token = access_token

    def upload_file(self , file_from , file_to):
        """ upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)     

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'IrqBeMNp4BgAAAAAAAAAAf53Q4XN-Ofitv1aeYredlFDqWtmuZEGoW6YiUcZ8-LU'
    transferData = TransferData(access_token)

    file_from = 'storage.txt'
    file_to = '/storage_dropbox/storage.txt'


    # API v2
    TransferData.upload_file(file_from , file_to)

if __name__=='__main__':
    main()    
