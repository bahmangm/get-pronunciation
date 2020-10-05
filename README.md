# get-pronunciation
a short python script to get a word in terminal and download its pronunciation from Oxford Dictionary

## How to use it
1. Create an account [here](https://developer.oxforddictionaries.com/) to get your **App ID** and **App Key**
2. Put the above items in the script
3. Mark the script as executable:
  *chmod +x pronunciation.py*
4. Add the dir containing it to your PATH variable:
  *export PATH=/path/to/script:$PATH*
5. Finally you can call it in the terminal in this form:  *pronunciation.py your_word*

The pronunciation of the word can be found as an mp3 file in the directory you have set in the script.
