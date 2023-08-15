# translator-python
 The purpose of this code is to read text from a file and translate it to Chinese or any other language  using the translate library from python, and save the translated text in a new file 
This code is a simple translation program that uses the Google Translate API. It takes a text file as input and outputs a translated version of the text in the specified language.

To use the program, first install the Google Translate API client library. You can do this by running the following command in a terminal window:

```
pip install googletrans
```

Once the library is installed, you can run the program by executing the following command:

```
python translate.py
```

This will open a dialog box where you can select the input file and the output language. Once you have selected the files, the program will start the translation process. The translated text will be output to a file called `japan.txt`.

Here is a step-by-step explanation of the code:

1. The first line imports the `Translator` class from the `translate` module.
2. The second line creates a new `Translator` object and sets the `to_lang` parameter to `zh` (Chinese).
3. The third line tries to open the input file. If the file does not exist, a `FileNotFoundError` exception is raised.
4. The fourth line reads the contents of the input file into a variable called `text`.
5. The fifth line calls the `translate()` method on the `Translator` object and passes the `text` variable as an argument. This returns a translated version of the text in the specified language.
6. The sixth line opens the output file and writes the translated text to the file.
7. The seventh line prints a message to the console if the file was not found.

I hope this helps!
