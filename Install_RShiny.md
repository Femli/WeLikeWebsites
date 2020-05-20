# Installing R and R Shiny Package
This is a short article to help you install the R programming language in your computer, and then install the R Shiny package. All in about 5 mins.

## Installing R
We will be installing the 4.0.0 version of R for Windows or Mac. Here are the steps:
- Click this [link](https://cran.r-project.org/mirrors.html)
- Scroll to USA and download from any link, such as [Oregon State University](https://ftp.osuosl.org/pub/cran/)
- Select your OS from the options: Window, Mac or Linux
  - For Mac, select R-4.0.0.pkg
  - For Windows, select the **base** option. Then select the **Download R 4.0.0 for Windows** option
- The installer should begin downloading at this point. Once completed, run it.
- Continue through the installation with the default settings.

That's it! R should now be installed. If using Mac, R should be in the applications folder. If using Windows, R should be in the Desktop as "R x64 4.0.0".

## Installing Shiny Package
Now that you have R installed, run it. There should be a window with the R Console on it. 
- In it, run the following command: `install.packages("shiny")`
- You will be prompted to select a CRAN mirror. Select any USA options, such as OR
- If you are prompted to "install from sources ... compilation", type yes
- A bunch of red text will apear. That's normal. Wait for it to finish.
- To test installation, in the R Console run `library(shiny)` followed by `runExample("01_hello")`
- A tab on your browser should appear with a web app showcasing R shiny.

Installation is now complete! Good job! :)
