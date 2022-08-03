from tkinter import messagebox as mb
import time, os, sys, ctypes


def CheckAdminRights(): #function to check if the program has admin rights
    import ctypes, os
    try:
     is_admin = os.getuid() == 0
    except AttributeError:
     is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return is_admin

has_admin = CheckAdminRights()
#has_admin = True
if has_admin == True:
    bloatware1 = ["echo hello", "echo world", "start-sleep -seconds 1"] # list of commands (test)

    bloatware = [ # list of commands (actual commands)
        "Get-AppxPackage *3DBuilder* | Remove-AppxPackage",
        "Get-AppxPackage *MicrosoftEdge* | Remove-AppxPackage",
        "Get-AppxPackage *Cortana* | Remove-AppxPackage",
        "Get-AppxPackage *WindowsPhone* | Remove-AppxPackage",
        "Get-AppxPackage *BingSports* | Remove-AppxPackage",
        "Get-AppxPackage *BingNews* | Remove-AppxPackage",
        "Get-AppxPackage *BingWeather* | Remove-AppxPackage",
        "Get-AppxPackage *BingFinance* | Remove-AppxPackage",
        "Get-AppxPackage *WindowsMaps* | Remove-AppxPackage",
        "Get-AppxPackage *Getstarted* | Remove-AppxPackage",
        "Get-AppxPackage *MicrosoftSolitaireCollection* | Remove-AppxPackage",
        ]

    bloatmsg = '''Would you like to remove the windows 10 Bloatware packages?

    Packages to be removed:
        *3DBuilder*
        *MicrosoftEdge*
        *Cortana*
        *WindowsPhone*
        *BingSports*
        *BingNews*
        *BingWeather*
        *BingFinance*
        *WindowsMaps*
        *Getstarted*
        *MicrosoftSolitaireCollection*
    '''

    

    mb.showinfo("Progress", "Deleting TEMP files...")
    time.sleep(1)
    os.system("del /q /s /f /a *.tmp")
    os.system("del %localappdata%\Temp")
    os.system("cleanmgr %systemroot%")
    mb.showinfo("Progress","Defragmenting system root disk...")
    os.system("defrag %systemroot%")
    mb.showinfo("Progress", "Searching and fixing corrupted files...")
    os.system("sfc /scannow")

    bloatwareremove = mb.askyesno("Bloatware Removal", bloatmsg)
    #bloatwareremove = "test" #test code
    if bloatwareremove == 'yes' or bloatwareremove == True:
        mb.showinfo('Progress', 'Removing Bloatware...')
        for i in bloatware:
            os.system("powershell "+i)
    elif bloatwareremove == 'no' or bloatwareremove == False:
        mb.showinfo('Response', 'No Bloatware will be removed.')
    else:
        mb.showwarning('Error', 'Something went wrong! What caused the issue: bloatwareremove variable is not a valid string nor boolean. Consider upgrading the appliacation and Python.')
        mb.showinfo("How to update", "You can update the application by going to the GitHub repository and downloading the latest version. Then, you can run the application again.")
        mb.showinfo("How to update python", "To update Python, you can go to the Python website and download the latest version. Then, you can run the application again.")
        mb.showwarning('Debug', 'bloatwareremove variable is: '+str(bloatwareremove))
        mb.showwarning('Debug', 'bloatwareremove variable type is: '+str(type(bloatwareremove)))
else:
    mb.showerror("Permission Error!","Please open this script as administrator to continue.")
