// create upload widget from cloudinary

// cloud and upload present names
const cloudName = "dxsxg4nkp";
const uploadPreset = "uw-test";

const myWidget = cloudinary.createUploadWidget(
  {
    cloudName: cloudName,
    uploadPreset: uploadPreset,
  },
  (error, result) => {
    if (!error && result && result.event === "success") {
      console.log("Done! Here is the image info: ", result.info);

      // display image preview
      let uploadedImage = document.getElementById("uploadedImage");
      uploadedImage.removeAttribute("hidden");

      // remove image required message and enable submit button
      document.getElementById("addImageRequired").remove();
      document.getElementById("addItemSubmit").removeAttribute("disabled");

      // upload and set thumbnail
      uploadedImage.setAttribute("src", result.info.secure_url);

      // set secure url attribute to my picture path ID
      document
        .getElementById("picture_path_id")
        .setAttribute("value", result.info.secure_url);
    }
  }
);

// event listener for upload widget button
document.getElementById("upload_widget").addEventListener(
  "click",
  function () {
    myWidget.open();
  },
  false
);

/* full list of possible parameters that you can add see: https://cloudinary.com/documentation/upload_widget_reference
   cropping: true, //add a cropping step
   showAdvancedOptions: true,  //add advanced options (public_id and tag)
   sources: [ "local", "url"], // restrict the upload sources to URL and local files
   multiple: false,  //restrict upload to a single file
   folder: "user_images", //upload files to the specified folder
   tags: ["users", "profile"], //add the given tags to the uploaded files
   context: {alt: "user_uploaded"}, //add the given context data to the uploaded files
   clientAllowedFormats: ["images"], //restrict uploading to image files only
   maxImageFileSize: 2000000,  //restrict file size to less than 2MB
   maxImageWidth: 2000, //Scales the image down to a width of 2000 pixels before uploading
   theme: "purple", //change to a purple theme */
