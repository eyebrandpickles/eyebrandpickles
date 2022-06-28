import instaloader
il = instaloader.Instaloader()
username = input("rajesh.photojourney")
il.download_profile(username , profile_pic_only=True)
print("Your DP is Downloaded")
