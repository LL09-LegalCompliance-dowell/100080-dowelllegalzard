let index = 0;
let updateIndex = 0;
let fileData = {};

document.addEventListener("DOMContentLoaded", function(event){

    const licenseImageEl = document.getElementById("license-image");
    const tableBodyEl = document.getElementById("table-body");
    const licenseBtnSaveEl = document.getElementById("btn-save-license");
    const licenseFormEl = document.getElementById("license-form");


    
    if(licenseImageEl){
        licenseImageEl.onchange = uploadFile;

        loadLicenseDropdown();
        loadCommonAttributeDropdown();
    }


    if(licenseBtnSaveEl){
        licenseBtnSaveEl.onclick = saveDataToDatabase;
    }

    if(tableBodyEl){
        loadTable();
    }


})


const uploadFile = (event) => {

    const licenseImageEl = document.getElementById("license-image");
    const processingImageSpinnerEl = document.getElementById("processing-image");
    const licenseImageViewContainerEl = document.getElementById("license-image-view-container");
    const licenseImageViewEl = document.getElementById("license-image-view");

    const formData = new FormData()
    formData.append('file', licenseImageEl.files[0])
    

    if (licenseImageEl.files && licenseImageEl.files[0]) {

        // preview image selected
        licenseImageViewContainerEl.style.display = "block"
        const reader = new FileReader();
        reader.onload = function (e) {
            licenseImageViewEl.setAttribute("src", e.target.result);
        };
        reader.readAsDataURL(licenseImageEl.files[0]);


        // BEGIN Processs image
        processingImageSpinnerEl.style.display = "block";
        fetch('/api/attachments/', {
            method: 'POST',
            body: formData
        }).then(response => {
            processingImageSpinnerEl.style.display = "none";
            if (response.status === 200){
                return response.json();
            }
    
        }).then(jsonData => {
            fileData = jsonData.file_data;
            console.log(fileData);
            
    
        }).catch(err => {
    
            console.log(err);
            processingImageSpinnerEl.style.display = "none";
        })
        // END process images


      }


}


const saveDataToDatabase = (event) =>{
    event.preventDefault();

    const formEl = document.getElementById("license-form");
    const errorContainerEl = document.querySelector("#error-container");
    const errorContentEl = document.querySelector("#error-content");
    const licenseEventId = formEl.getAttribute("data-event-id");
    const methodType = formEl.getAttribute("data-method-type");
 
    const licenseDescription = document.querySelector("#license-description").value;
    const shortDescription = document.querySelector("#short-description").value;
    const licenseName = document.querySelector("#license-name").value;
    const version = document.querySelector("#version").value;
    const typeOfLicense = document.querySelector("#type-of-license").value;
    const licenseUrl = document.querySelector("#license-url").value;
    const disclaimer = document.querySelector("#disclaimer").value;
    const riskForChoosingLicense = document.querySelector("#risk-for-choosing-license").value;
    const limitationOfLiability = document.querySelector("#limitation-of-liability").value;
    const licenseAttributeHeading = document.querySelector("#license-attribute-heading").value;
    const licenseAttribute = document.querySelectorAll('#license-attribute option:checked');
    const licenseCompatibleWith = document.querySelectorAll('#license-compatible-with option:checked');
    const licenseNotCompatibleWith = document.querySelectorAll('#license-not-compatible-with option:checked');
    const btnSaveData = document.querySelector("#btn-save-license");




    // reset error 
    errorContainerEl.style.display = "none";
    errorContentEl.textContent = "";

    console.log("I am called")

    if (validateInput()){

        console.log("I am valid")
        // Activate loading
        const loading = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> saving...';
        btnSaveData.innerHTML = loading;
        btnSaveData.disabled = true;

        const licenseNotCompatibleWithList = [];
        for (let option of licenseNotCompatibleWith) {
            licenseNotCompatibleWithList.push(option.value);
        } 
        
        const licenseCompatibleWithList = [];
        for (let option of licenseCompatibleWith) {
            licenseCompatibleWithList.push(option.value);
        }

        const licenseAttributeList = [];
        for (let option of licenseAttribute) {
            licenseAttributeList.push(option.value);
        }

        // Format data
        const data = {
            features: [],
            other_links: [],
            license_name: licenseName,
            version: version,
            license_url: licenseUrl,
            type_of_license: typeOfLicense,
            short_description: shortDescription,
            description: licenseDescription,
            disclaimer: disclaimer,
            risk_for_choosing_license: riskForChoosingLicense,
            limitation_of_liability: limitationOfLiability,
            logo_detail: {
                filename: fileData.filename,
                actual_filename: fileData.actual_filename,
                file_extension: fileData.file_extension,
                url: ""
            },
            recommendation: " ",
            license_attributes: {
                heading: licenseAttributeHeading,
                attributes: licenseAttributeList
            },
            license_compatible_with_lookup: licenseCompatibleWithList,
            license_not_compatible_with_lookup: licenseNotCompatibleWithList
        }


        let url = "/api/licenses/";
        if (methodType === "PUT")
        {
            url = "/api/licenses/"+licenseEventId+"/";
        }


        fetch(url, {
            method: methodType,
            body: JSON.stringify(data),
            headers: {"Content-Type": "application/json"}
        }).then(function(response){
            if (response.status === 201 || response.status === 200){

                window.location.href = "/temp-admin/licenses/";

            }else{


                // set error 
                errorContainerEl.style.display = "block";
                errorContentEl.textContent = "Something went wrong, whilst saving the data!";

                // deactivate loading
                btnSaveData.innerHTML = "Save";
                btnSaveData.disabled = false;


            }

        }).catch(function(err){

            // set error 
            errorContainerEl.style.display = "block";
            errorContentEl.textContent = "Something went wrong, check your network!";

            // deactivate loading
            btnSaveData.innerHTML = "Save";
            btnSaveData.disabled = false;

        })
        



    }


}



const loadTable = () => {
   
    const tableSpinnerEl = document.getElementById("table-spinner");
    const tableBodyEl = document.getElementById("table-body");

    fetch("/api/licenses/", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }else{
            tableSpinnerEl.style.display = "none";
        }

    }).then(function(jsonData){

    
        let content = "";
        index = 0;

        for (let license of jsonData.data){
            index += 1;
            content += tableContent(index, license);
            console.log(content);
        }

        tableSpinnerEl.style.display = "none";
        tableBodyEl.innerHTML = content;
        document.getElementById("btn-add-new").style.display = "inline-block";
        // listenToEditBtn();
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}

const loadLicenseDetailForUpdate = (licenseEventId) => {

    document.getElementById("page-spinner").style.display = "block";
    document.getElementById("license-form").style.display = "none";
    const licenseDescription = document.querySelector("#license-description")
    const shortDescription = document.querySelector("#short-description")
    const licenseName = document.querySelector("#license-name")
    const version = document.querySelector("#version")
    const typeOfLicense = document.querySelector("#type-of-license")
    const licenseUrl = document.querySelector("#license-url")
    const disclaimer = document.querySelector("#disclaimer")
    const riskForChoosingLicense = document.querySelector("#risk-for-choosing-license")
    const limitationOfLiability = document.querySelector("#limitation-of-liability")
    const licenseAttributeHeading = document.querySelector("#license-attribute-heading")
    // const licenseAttribute = document.querySelector('#license-attribute');
    // const licenseCompatibleWith = document.querySelector('#license-compatible-with');
    // const licenseNotCompatibleWith = document.querySelector('#license-not-compatible-with');


    const licenseImageViewContainerEl = document.getElementById("license-image-view-container");
    const licenseImageViewEl = document.getElementById("license-image-view");

    fetch("/api/licenses/"+licenseEventId+"/", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }else{
            tableSpinnerEl.style.display = "none";
        }

    }).then(function(jsonData){

        const data = jsonData.data[0];
        const license = data.softwarelicense;
        fileData = license.logo_detail;


        licenseDescription.innerHTML = license.description;
        shortDescription.value = license.short_description;
        licenseName.value = license.license_name;
        version.value = license.version;
        typeOfLicense.value = license.type_of_license;
        licenseUrl.value = license.license_url;
        disclaimer.value = license.disclaimer;
        riskForChoosingLicense.value = license.risk_for_choosing_license;
        limitationOfLiability.value = license.limitation_of_liability;
        licenseAttributeHeading.value = license.license_attributes.heading;
        licenseImageViewEl.setAttribute("src", license.logo_detail.url);
        licenseImageViewContainerEl.style.display = "block";

        $("#license-attribute").val(license.license_attributes.attributes);
        $("#license-compatible-with").val(license.license_compatible_with_lookup);
        $("#license-not-compatible-with").val(license.license_not_compatible_with_lookup);
        

        document.getElementById("page-spinner").style.display = "none";
        document.getElementById("license-form").style.display = "block";



    }).catch(function(err){
        document.getElementById("page-spinner").style.display = "none";
        document.getElementById("license-form").style.display = "block";

    })


    

}


const loadLicenseDropdown = () => {

    fetch("/api/licenses/", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }
    }).then(function(jsonData){

    
        let content = '<option selected>None</option>';
        const licenseNotCompatibleWithEl = document.getElementById("license-not-compatible-with");
        const licenseCompatibleWithEl = document.getElementById("license-compatible-with");

        for (let license of jsonData.data){
            content += `<option value="${license.softwarelicense.license_name}">${license.softwarelicense.license_name} (${license.softwarelicense.version})</option>`;
        }

        licenseCompatibleWithEl.innerHTML = content;
        licenseNotCompatibleWithEl.innerHTML = content;


        // Load license detail
        // methodType is PUT
        const licenseFormEl = document.getElementById("license-form");
        const methodType = licenseFormEl.getAttribute("data-method-type")
        if(licenseFormEl){

            if(methodType === "PUT"){
                const licenseEventId = licenseFormEl.getAttribute("data-event-id");
                loadLicenseDetailForUpdate(licenseEventId);
            }else{
                document.getElementById("license-form").style.display = "block";
                document.getElementById("page-spinner").style.display = "none";
            }

        }

        

    }).catch(function(err){
        document.getElementById("page-spinner").style.display = "none";

    })


    

}


const loadCommonAttributeDropdown = () => {
   

    fetch("/api/commonattributes/", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }
    }).then(function(jsonData){

    
        let content = '<option selected>None</option>';
        const licenseAttributeEl = document.getElementById("license-attribute");

        for (let commomAttribute of jsonData.data){
            content += `<option value="${commomAttribute.common_attributes.name}">${commomAttribute.common_attributes.name}</option>`;
        }

        licenseAttributeEl.innerHTML = content;
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}


const tableContent = (index, data) => {
    license = data.softwarelicense;

    let imageUrl = "";
    if ("undefined" === typeof (license["logo_detail"])) {
        imageUrl = "#";
      }else{
        imageUrl = license.logo_detail.url;
      }
    
    return `
            <tr>
                  <td scope="row">${index}</td>
                  <td>${license.license_name}</td>
                  <td>${license.version}</td>
                  <td><img src="${imageUrl}" height="50px" alt="${license.license_name}"></td>
                  <td style="width: 10px;">

                    <div class="btn-group" role="group" aria-label="action">
                        <a href="/temp-admin/license-edit/${data.eventId}/" data-id="${data.eventId}"  class="btn btn-primary">Edit</a>
                    </div>

                  </td>
            </tr>    
            `
}



const validateInput = () => {
    let isValid = true;

    const licenseDescription = document.querySelector("#license-description").value;
    const licenseName = document.querySelector("#license-name").value;
    const version = document.querySelector("#version").value;
    const typeOfLicense = document.querySelector("#type-of-license").value;
    const licenseUrl = document.querySelector("#license-url").value;
    const licenseAttributeHeading = document.querySelector("#license-attribute-heading").value;
    const licenseAttribute = document.querySelectorAll("#license-attribute  option:checked");
    const licenseCompatibleWith = document.querySelectorAll("#license-compatible-with  option:checked");

    
    const licenseCompatibleWithList = [];
    for (let option of licenseCompatibleWith) {
        licenseCompatibleWithList.push(option.value);
    }

    const licenseAttributeList = [];
    for (let option of licenseAttribute) {
        licenseAttributeList.push(option.value);
    }
    console.log(licenseCompatibleWithList)
    console.log(licenseAttributeList)



    const licenseNameErrorEl = document.querySelector("#license-name-error");
    const versionErrorEl = document.querySelector("#version-error");
    const typeOfLicenseErrorEl = document.querySelector("#type-of-license-error");
    const licenseUrlErrorEl = document.querySelector("#license-url-error");
    const licenseAttributeHeadingErrorEl = document.querySelector("#license-attribute-heading-error");
    const licenseAttributeErrorEl = document.querySelector("#license-attribute-error");
    const licenseCompatibleWithErrorEl = document.querySelector("#license-compatible-with-error");
    const descriptionErrorEl = document.querySelector("#description-error");
    const licenseImageErrorEl = document.querySelector("#license-image-error");

    if (licenseName === ""){
        isValid = false;
        licenseNameErrorEl.style.display = "block";
    }else{
        licenseNameErrorEl.style.display = "none";
    }

    if (version === ""){
        isValid = false;
        versionErrorEl.style.display = "block";
    }else{
        versionErrorEl.style.display = "none";
    }

    if (typeOfLicense === ""){
        isValid = false;
        typeOfLicenseErrorEl.style.display = "block";
    }else{
        typeOfLicenseErrorEl.style.display = "none";
    }


    if (licenseUrl === ""){
        isValid = false;
        licenseUrlErrorEl.style.display = "block";
    }else{
        licenseUrlErrorEl.style.display = "none";
    }

    if (licenseAttributeHeading === ""){
        isValid = false;
        licenseAttributeHeadingErrorEl.style.display = "block";
    }else{
        licenseAttributeHeadingErrorEl.style.display = "none";
    }


    if (licenseAttributeList){
        licenseAttributeErrorEl.style.display = "none";
    }else{
        isValid = false;
        licenseAttributeErrorEl.style.display = "block";
    }

    if (licenseCompatibleWithList){
        licenseCompatibleWithErrorEl.style.display = "none";
    }else{
        isValid = false;
        licenseCompatibleWithErrorEl.style.display = "block";
    }

    if (licenseDescription === ""){
        isValid = false;
        descriptionErrorEl.style.display = "block";
    }else{
        descriptionErrorEl.style.display = "none";
    }

    if (fileData){
        licenseImageErrorEl.style.display = "none";
    }else{
        isValid = false;
        licenseImageErrorEl.style.display = "block";       
    }



    return isValid;
}