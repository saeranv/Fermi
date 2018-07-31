# To add a Revit Application as a Add-in

1. Add RevitAPI.dll, RevitAPIUI.dll, from the version of Revit to the references.
2. Add the Addin manifest in the Revit 2018/Addin dir
3. Copy and paste the application dll, and all dependencies (whatever is generated from the Visual Studio Debug)
4. This should work for the Addin tab. To get it to work from the Addin manager
5. Add the Addin.addin, and addin.dll, from the Revit SDK.
