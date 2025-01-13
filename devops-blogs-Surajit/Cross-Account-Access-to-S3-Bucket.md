1. Create a bucket policy for a S3 Bucket that you need to give cross account access.
```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "Cross Region Bucket Access",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::<dest_ac_id>:root"
         },
         "Action": [
            "s3:GetLifecycleConfiguration",
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::surajit-s3-bucket"
         ]
      }
   ]
}
```
2. Create a IAM Policy with the 'List Bucket' access to the destination account. 
```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "Cross Region Bucket Access Policy",
         "Effect": "Allow",
         "Action": [
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::surajit-s3-bucket"
         ]
      }
   ]
}
```
3. Attach the policy to the destination account user.

4. Test the access by below command -
   
``` aws s3 ls s3://<bucket_name> --profile <profile_name> ```
