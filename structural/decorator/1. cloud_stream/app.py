from cloud_stream import CloudStream
from ecrypted_cloud_stream import EncryptedCloudStream
from compressed_cloud_stream import CompressedCloudStream


def store_credit_card(stream):
    stream.write('1234-1234-1234-1234')


store_credit_card(EncryptedCloudStream(CompressedCloudStream(CloudStream())))
