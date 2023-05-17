#!/usr/bin/env python
# coding: utf-8

# In[1]:


from instabot import Bot

bot = Bot() #calling Bot function 

username = input("Enter your username") #enter your username for login
password = input("Enter your password") # enter you own password of insta 
bot.login(username=username, password=password) #function for login to insta account

while True:   #this loop will be run untill you choose option to logout
    print("MENU")
    print("______________________________________")
    print(" 1.Follow an account")
    print(" 2.Unfollow an account")
    print(" 3.Upload a post with a caption")
    print(" 4.Like recent post of a user")
    print(" 5.Send a direct message to an user")
    print(" 6.Block an account")
    print(" 7.Unblock an account")
    print("________________________________________")

    choice = input("Enter your choice (1-8): ")
    

    if choice == "1":
        target_user = input("Enter the username of the account you want to follow!: ")
        bot.follow(target_user)
        print("You have followed", target_user)
    
    elif choice == "2":
        target_user = input("Enter the username of the account you want to unfollow!: ")
        bot.unfollow(target_user)
        print("You have unfollowed", target_user)

    elif choice == "3":
        image_path = input("Enter the image path!: ")
        caption = input("Enter the caption!")
        bot.upload_photo(image_path, caption=caption)
        print("Your post has been uploaded!!")
    
    elif choice == "4":
        target_user = input("Enter the usrname of the account you want to like recent post: ")
        bot.like_user(target_user, amount=3)
        print("You have liked the recent post of", target_user)
    
    elif choice == "5":
        target_user = input("Enter the username of account you want to send message: ")
        msg = input("Enter the message: ")
        bot.send_message(msg, target_username)
        print("Your msg has been sent!!")
    
    elif choice == "6":
        target_user = input("Enter the username of account you want to block: ")
        bot.block(target_user)
        print("You have blocked", target_user)
    
    elif choice == "7":
        target_user = input("Enter the username of account you want to unblock: ")
        bot.unblock(target_user)
        print("You haave unblocked", target_user)
    
    elif choice == "8":
        bot.logout()
        print("You are successfully logout!")
        break
    
    
    else:
        print("Invalid choice")
        
#if you want, you can add more function grom instabot library!!

    



    
    
    


# In[ ]:





# In[ ]:




