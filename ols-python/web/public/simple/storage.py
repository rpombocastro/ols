# SI QUEREMOS UTILIZAR EL SISMTEMA DE ALMACENAMIENTO DE S3 PARA ARCHIVOS STATIC, MEDIA O UNO DE ELLOS
# DEBEMOS UTILIZAR ESTA PÁGINA E INSTALAR EL PAQUETE BOTO3
# pip install boto3 (Se hizo con esta version boto3==1.29.7)

# import boto3

# from django.conf import settings
# from storages.backends.s3boto3 import S3StaticStorage, S3Boto3Storage

# class StaticStorage(S3StaticStorage):
#     location = settings.AWS_STATIC_LOCATION
#     default_acl = 'public-read'

# class PublicMediaStorage(S3Boto3Storage):
#     location = settings.AWS_MEDIA_LOCATION
#     default_acl = 'public-read'
#     file_overwrite = False

# class PrivateMediaStorage(S3Boto3Storage):
#     location = settings.AWS_MEDIA_LOCATION
#     default_acl = 'private'
#     file_overwrite = False


# def s3_remove_media_file(file_name):
#     client = boto3.client('s3', 
#                           aws_access_key_id = settings.AWS_ACCESS_KEY_ID, 
#                           aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY, 
#                           endpoint_url = settings.AWS_S3_ENDPOINT_URL)
    
#     bucket_name = settings.AWS_STORAGE_BUCKET_NAME
#     file_path = settings.AWS_MEDIA_LOCATION + '/' + file_name

#     client.delete_object(Bucket=bucket_name, Key=file_path)

# def s3_generate_private_url(file_name):

#     client = boto3.client('s3', 
#                             aws_access_key_id = settings.AWS_ACCESS_KEY_ID, 
#                             aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY, 
#                             endpoint_url = settings.AWS_S3_ENDPOINT_URL)
        
#     bucket_name = settings.AWS_STORAGE_BUCKET_NAME
#     file_path = settings.AWS_MEDIA_LOCATION + '/' + file_name
    
#     url = client.generate_presigned_url(
#                                     'get_object',
#                                     Params = { 
#                                             'Bucket': bucket_name, 
#                                             'Key': file_path
#                                             }, 
#                                     ExpiresIn = 60)
    
#     return url