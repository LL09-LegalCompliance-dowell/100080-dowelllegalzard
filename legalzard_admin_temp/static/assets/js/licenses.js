let index = 0;
let updateIndex = 0;
let fileData = {};
let licenseTagAddCount = 0;
let licenseReferenceAddCount = 0;
let responseStatus = 400;
let licensePermissionAddCount = 0;
let licenseConditionAddCount = 0;
let licenseLimitationAddCount = 0;
let licenseLawAddCount = 0;
let licenseSourceAddCount = 0;
let licenseMustIncludeAddCount = 0;

const permissionData = [
    "Patent Use",
    "Private Use",
    "Patent Grant",
    "Distribution",
    "Modification",
    "Commercial Use",
    "Place Warranty",
    "Trademark Grant"
]
let permissionSelectOption = "";

const conditionData = [
    "Copied",
    "Modified",
    "Reproduced",
    "Distributed",
    "State Changes",
    "Commercial Used",
    "Disclose Source Code",
    "Release Under Same License",
    "Network Use is for Distribution",
    "Code can be used in closed source project"
]
let conditionSelectOption = "";

const limitationData = [
    "Liability",
    "Warranty",
    "Trademark use",
    "Redistribution"
]
let limitationSelectOption = "";

const sourceData = [
    "FSF Approved",
    "OSI Approved"
]
let sourceSelectOption = "";

const mustIncludeData = [
    "License",
    "Copyright Notice"
]
let mustIncludeOption = "";



document.addEventListener("DOMContentLoaded", function(event){

    const licenseImageEl = document.getElementById("license-image");
    const tableBodyEl = document.getElementById("table-body");
    const licenseBtnSaveEl = document.getElementById("btn-save-license");
    const licenseTagAddEl = document.getElementById("btn-add-license-tag");
    const licenseReferenceAddEl = document.getElementById("btn-add-references");
    const licensePermissionAddEl = document.getElementById("btn-add-permissions");
    const licenseConditionAddEl = document.getElementById("btn-add-conditions");
    const licenseLimitationAddEl = document.getElementById("btn-add-limitations");
    const licenseSourceAddEl = document.getElementById("btn-add-source");


    
    if(licenseImageEl){
        licenseImageEl.onchange = uploadFile;

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

    }


    if(licenseBtnSaveEl){
        licenseBtnSaveEl.onclick = saveDataToDatabase;
    }

    if(licenseTagAddEl){
        licenseTagAddEl.onclick = function(event){
            formatAddTag("", "");
        };
    }

    if(licenseReferenceAddEl){
        licenseReferenceAddEl.onclick = function(event){
            formatAddReference("", "");
        };
    }
    // 
    if(licensePermissionAddEl){
        licensePermissionAddEl.onclick = function(event){
            formatAddPermission("", "");
        };
    }

    if(licenseConditionAddEl){
        licenseConditionAddEl.onclick = function(event){
            formatAddCondition("", "");
        };
    }

    if(licenseLimitationAddEl){
        licenseLimitationAddEl.onclick = function(event){
            formatAddLimitation("", "");
        };
    }

    if(licenseSourceAddEl){
        licenseSourceAddEl.onclick = function(event){
            formatAddSource("", "");
        };
    }


    if(tableBodyEl){
        loadTable();
    }



    // BEGIN delete of license detail
    deleteLicenseConfirmEl = document.querySelector("#confirm-delete");
    if (deleteLicenseConfirmEl) {

        deleteLicenseConfirmEl.addEventListener("click", function(event){

            const spinner = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                        Deleting...`
    
    
            const eventId = document.getElementById("confirm-delete").getAttribute("data-id");
            const licenseName = document.getElementById("confirm-delete").getAttribute("data-license-name");
            this.innerHTML = spinner;
            const errorEl = document.getElementById("delete-license-error-notify");
            errorEl.innerHTML = "";
    
            fetch(`/api/licenses/${eventId}/`, {
                    method: "DELETE",
                    headers: {"Content-Type": "application/json"}
                }).then(response => {
    
                    if (response.status === 200){
                        const licenseDetailContentEl = document.getElementById(`license-table-row-${eventId}`)
                        licenseDetailContentEl.remove();
                        this.innerHTML = "Delete";
                        document.getElementById("delete-license-modal-close").click();
    
                    }else {
    
                        this.innerHTML="Delete";
                        response.json()
                    }
    
                }).then(jsonData => {
    
                    errorEl.innerHTML = jsonData.error_msg;
    
                }).catch(error => {
    
                })
            })
            // END delete of license detail

    }



    // Select Option Content
    permissionSelectOption = permissionData.map((data, index) => {

        return `<option value="${data}">${data}</option>`;
    })

    conditionSelectOption = conditionData.map((data, index) => {

        return `<option value="${data}">${data}</option>`;
    })

    limitationSelectOption = limitationData.map((data, index) => {

        return `<option value="${data}">${data}</option>`;
    })

    sourceSelectOption = sourceData.map((data, index) => {

        return `<option value="${data}">${data}</option>`;
    })

    mustIncludeOption = mustIncludeData.map((data, index) => {

        return `<option value="${data}">${data}</option>`;
    })


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
    const btnSaveData = document.querySelector("#btn-save-license");
    // const mustIncludes = document.querySelectorAll('#must-includes option:checked');
    const laws = document.querySelector("#law").value;





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

        // Format data
        const data = {
            features: [],
            other_links: [],
            license_name: licenseName,
            version: version,
            license_url: licenseUrl,
            type_of_license: typeOfLicense,
            license_tags: [],
            short_description: sanitizeText(shortDescription),
            description: sanitizeText(licenseDescription),
            disclaimer: sanitizeText(disclaimer),
            risk_for_choosing_license: sanitizeText(riskForChoosingLicense),
            limitation_of_liability: sanitizeText(limitationOfLiability),
            logo_detail: {
                filename: fileData.filename,
                actual_filename: fileData.actual_filename,
                file_extension: fileData.file_extension,
                url: ""
            },
            recommendation: " ",
            permissions: getLicenseCompatibilityAttributeContent("permission"),
            conditions: getLicenseCompatibilityAttributeContent("condition"),
            limitations: getLicenseCompatibilityAttributeContent("limitation"),
            sources: getLicenseCompatibilityAttributeContent("source"),
            must_includes: getLicenseCompatibilityAttributeContent("must-include"),
            laws: laws,
            references: getLicenseReferenceContent()
            
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

            responseStatus = response.status;
            if (response.status === 201 || response.status === 200){

                window.location.href = "/temp-admin/licenses/";

            }else{

                return response.json();

            }

        }).then(jsonData => {

            if(typeof jsonData === 'undefined') {
                console.log('Return object is either the special value `undefined`, or it has not been declared');
            }else{
               // set error 
               errorContainerEl.style.display = "block";
               errorContentEl.textContent = jsonData.error_msg;

               // deactivate loading
               btnSaveData.innerHTML = "Save";
               btnSaveData.disabled = false;
            }
 

        }).catch(function(err){

            // set error 
            console.log(err)
            errorContainerEl.style.display = "block";
            errorContentEl.textContent = err.toString();

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
        }

        tableSpinnerEl.style.display = "none";
        tableBodyEl.innerHTML = content;
        document.getElementById("btn-add-new").style.display = "inline-block";
        // listenToEditBtn();
        deleteLicense();

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
        licenseImageViewEl.setAttribute("src", license.logo_detail.url);
        licenseImageViewContainerEl.style.display = "block";


        $("#must-includes").val(license.must_includes);
        $("#law").val(license.laws);


        // display license references
        if(license["references"] !== undefined){

            license.references.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                formatAddReference(action, permission);
            })
        }

        // display license permissions
        if(license["permissions"] !== undefined){

            license.permissions.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                let hasOtherCondition = false;
                if (data["has_other_condition"] !== undefined){
                    hasOtherCondition = data["has_other_condition"];
                }
                formatAddPermission(action, permission, hasOtherCondition);
            })
        }

        // display license conditions
        if(license["conditions"] !== undefined){

            license.conditions.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                let hasOtherCondition = false;
                if (data["has_other_condition"] !== undefined){
                    hasOtherCondition = data["has_other_condition"];
                }
                formatAddCondition(action, permission, hasOtherCondition);
            })
        }

        // display license limitations
        if(license["limitations"] !== undefined){

            license.limitations.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                let hasOtherCondition = false;
                if (data["has_other_condition"] !== undefined){
                    hasOtherCondition = data["has_other_condition"];
                }
                formatAddLimitation(action, permission, hasOtherCondition);
            })
        }
        
        // display license source
        if(license["sources"] !== undefined){

            license.sources.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                formatAddSource(action, permission);
            })
        }

        // display license must_includes
        if(license["must_includes"] !== undefined){

            license.sources.forEach(data => {
                const action = data["action"];
                const permission = data["permission"];
                formatAddMustInclude(action, permission);
            })
        }


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
   

    fetch("/api/attributes/", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }
    }).then(function(jsonData){

    
        let content = '<option selected>None</option>';
        const licenseAttributeEl = document.getElementById("license-attribute");

        for (let attribute of jsonData.data){
            if(attribute.attributes.hasOwnProperty("name")){
                content += `<option value="${attribute.attributes.name}">${attribute.attributes.name}</option>`;
            }
        }

        licenseAttributeEl.innerHTML = content;


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
            <tr id="license-table-row-${data.eventId}">
                  <td scope="row">${index}</td>
                  <td>${license.license_name}</td>
                  <td>${license.version}</td>
                  <td><img src="${imageUrl}" height="50px" alt="${license.license_name}"></td>
                  <td style="width: 10px;">
                    <div class="btn-group" role="group" aria-label="action">
                        <a href="/temp-admin/license-edit/${data.eventId}/" data-id="${data.eventId}"  class="btn btn-primary">Edit</a>
                        <a href="#" data-license-version="${license.version}" data-license-name="${license.license_name}"   data-id="${data.eventId}" data-bs-toggle="modal" data-bs-target="#delete-license-modal" class="btn btn-danger delete-license">Delete</a>
                    </div>
                  </td>
            </tr>    
            `
}



const validateInput = () => {
    let isValid = true;


    const licenseName = document.querySelector("#license-name").value;
    const version = document.querySelector("#version").value;
    const typeOfLicense = document.querySelector("#type-of-license").value;
    const licenseUrl = document.querySelector("#license-url").value;

    const licenseNameErrorEl = document.querySelector("#license-name-error");
    const versionErrorEl = document.querySelector("#version-error");
    const typeOfLicenseErrorEl = document.querySelector("#type-of-license-error");
    const licenseUrlErrorEl = document.querySelector("#license-url-error");
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

    if (fileData){
        licenseImageErrorEl.style.display = "none";
    }else{
        isValid = false;
        licenseImageErrorEl.style.display = "block";       
    }


    return isValid;

}


const formatAddTag = (key="", value="") => {
    licenseTagAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-3 other-info">
        <input type="text"  placeholder="Enter Key" class="form-control" value="${key}" id="license-tags-${licenseTagAddCount}-key">
        </div>

        <div style="display: inline-block;" class="col-7 other-info">
        <input type="text" class="form-control" placeholder="Enter Value" value="${value}" id="license-tags-${licenseTagAddCount}-value">
        </div>
        <div style="display: inline-block;" class="col-1 other-info">
        <button type="button" data-tag-id="license-tags-${licenseTagAddCount}" class="btn btn-outline-danger license-tags-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-tags-${licenseTagAddCount}`);
    divEl.setAttribute('data-tag-id', `license-tags-${licenseTagAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-tags`);
    divEl.innerHTML = content;
    const licenseTagsContainerEl = document.getElementById("license-tags-container")
    licenseTagsContainerEl.appendChild(divEl);
    deleteLicenseTag();
}

const deleteLicenseTag = () => {
    const licenseTagsDeleteEl = document.querySelectorAll(".license-tags-delete");
    licenseTagsDeleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            document.querySelector(`#${tagId}`).remove();
        }

    });
}


const getLicenseTagContent = () => {

    const licenseTags = [];
    
    const licenseTagsEl = document.querySelectorAll(".license-tags");
    licenseTagsEl.forEach(element => {
        const tagId = element.getAttribute("data-tag-id");
        let key = document.querySelector(`#${tagId}-key`).value;
        const value = document.querySelector(`#${tagId}-value`).value;

        if (value && key){

            // format data
            key = key.replace(":", "").trim();
            const data = {};
            data[key] = value.trim();

            licenseTags.push(data);

        }


    })

    return licenseTags;
}

const getLicenseReferenceContent = () => {

    const licenseReferences = [];
    
    const licenseReferenceEl = document.querySelectorAll(".license-reference");
    licenseReferenceEl.forEach(element => {
        const referenceId = element.getAttribute("data-reference-id");
        let key = document.querySelector(`#${referenceId}-key`).value;
        const value = document.querySelector(`#${referenceId}-value`).value;

        if (value && key){

            // format data
            key = key.replace(":", "").trim();
            const data = {};
            data["action"] = key.trim();
            data["permission"] = value.trim();

            licenseReferences.push(data);

        }


    })

    return licenseReferences;
}


const formatAddReference = (action="", permission="") => {
    licenseReferenceAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-7 other-info">
        <input type="text"  placeholder="Enter value" class="form-control" value="${action}" id="license-reference-${licenseReferenceAddCount}-key">
        </div>

        <div style="display: inline-block;" class="col-3 other-info">
            <select required class="form-select" id="license-reference-${licenseReferenceAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>
        <div style="display: inline-block;" class="col-1 other-info">
        <button type="button" data-reference-id="license-reference-${licenseReferenceAddCount}" class="btn btn-outline-danger license-reference-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-reference-${licenseReferenceAddCount}`);
    divEl.setAttribute('data-reference-id', `license-reference-${licenseReferenceAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-reference`);
    divEl.innerHTML = content;
    const licenseReferenceContainerEl = document.getElementById("license-reference-container")
    licenseReferenceContainerEl.appendChild(divEl);
    if(permission){
        document.getElementById(`license-reference-${licenseReferenceAddCount}-value`).value = permission;
    }

    deleteLicenseReference();
}

const deleteLicenseReference = () => {
    const licenseReferenceDeleteEl = document.querySelectorAll(".license-reference-delete");
    licenseReferenceDeleteEl.forEach(element => {

        element.onclick = function(event){
            const referenceId = element.getAttribute("data-reference-id");
            document.querySelector(`#${referenceId}`).remove();
        }

    });
}


const deleteLicense = () => {
    console.log("worl")
    const deleteBtnEls = document.querySelectorAll(".delete-license");
    // loop over all delete button
    // and event listener to it
    deleteBtnEls.forEach(element => {

      element.addEventListener("click", function(event){


        const eventId = this.getAttribute("data-id");
        const licenseName = this.getAttribute("data-license-name");
        const licenseVersion = this.getAttribute("data-license-version");
        console.log(licenseName);

        document.getElementById("delete-license-name").innerHTML=`license: ${licenseName}, version: ${licenseVersion}`;
        const deleteBtnEl = document.getElementById("confirm-delete");
        deleteBtnEl.setAttribute("data-license-name", licenseName);
        deleteBtnEl.setAttribute("data-id", eventId);
      });

    });
  }

const sanitizeText = (text) => {
    return text.replace(/["${}]/g,"");
}



// Permission
const formatAddPermission = (action="", permission="", has_other_condition=false) => {
    licensePermissionAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-4 other-info">
            <select required class="form-select" id="license-permission-${licensePermissionAddCount}-key">
            ${permissionSelectOption}
            </select>
        </div>

        <div style="display: inline-block;" class="col-2 other-info">
            <select required class="form-select" id="license-permission-${licensePermissionAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>

        <div style="display: inline-block; margin-left: 20px;" class="col-4 other-info">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="license-permission-${licensePermissionAddCount}-has-condition">
                <label class="form-check-label" for="gridCheck1">
                    Has condition
                </label>
            </div>
        </div>

        <div style="display: inline-block;" class="col-1 other-info">
        <button type="button" data-tag-id="license-permission-${licensePermissionAddCount}" class="btn btn-outline-danger license-permission-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-permission-${licensePermissionAddCount}`);
    divEl.setAttribute('data-tag-id', `license-permission-${licensePermissionAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-permission`);
    divEl.innerHTML = content;
    const containerEl = document.getElementById("license-permission-container")
    containerEl.appendChild(divEl);

    if(action){
        document.getElementById(`license-permission-${licensePermissionAddCount}-key`).value = action;
    }
    if(permission){
        document.getElementById(`license-permission-${licensePermissionAddCount}-value`).value = permission;
    }
    document.getElementById(`license-permission-${licensePermissionAddCount}-has-condition`).checked = has_other_condition;

    deleteLicensePermission();
}

const deleteLicensePermission = () => {
    const deleteEl = document.querySelectorAll(".license-permission-delete");
    deleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            console.log(tagId)
            document.querySelector(`#${tagId}`).remove();
        }

    });
}

const getLicenseCompatibilityAttributeContent = (selected) => {

    const licenseOtherAttributes = [];
    
    const licenseReferenceEl = document.querySelectorAll(`.license-${selected}`);
    licenseReferenceEl.forEach(element => {
        const id = element.getAttribute(`data-tag-id`);
        console.log(id)
        let key = document.querySelector(`#${id}-key`).value;
        const value = document.querySelector(`#${id}-value`).value;
        const hasConditon = document.querySelector(`#${id}-has-condition`);

        if (value && key){

            // format data
            key = key.replace(":", "").trim();
            const data = {};
            data["action"] = key.trim();
            data["permission"] = value.trim();
            if(hasConditon){
                data["has_other_condition"] = hasConditon.checked;
            }
            licenseOtherAttributes.push(data);

        }


    })

    return licenseOtherAttributes;
}


// Condition
const formatAddCondition = (action="", permission="", has_other_condition=false) => {
    licenseConditionAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-4 other-info">
            <select required class="form-select" id="license-condition-${licenseConditionAddCount}-key">
            ${conditionSelectOption}
            </select>
        </div>

        <div style="display: inline-block;" class="col-2 other-info">
            <select required class="form-select" id="license-condition-${licenseConditionAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>

        <div style="display: inline-block; margin-left: 20px;" class="col-4 other-info">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="license-condition-${licenseConditionAddCount}-has-condition">
                <label class="form-check-label" for="gridCheck1">
                    Has condition
                </label>
            </div>
        </div>

        <div style="display: inline-block;" class="col-1 other-info">
            <button type="button" data-tag-id="license-condition-${licenseConditionAddCount}" class="btn btn-outline-danger license-condition-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-condition-${licenseConditionAddCount}`);
    divEl.setAttribute('data-tag-id', `license-condition-${licenseConditionAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-condition`);
    divEl.innerHTML = content;
    const containerEl = document.getElementById("license-condition-container")
    containerEl.appendChild(divEl);

    if(action){
        document.getElementById(`license-condition-${licenseConditionAddCount}-key`).value = action;
    }
    if(permission){
        document.getElementById(`license-condition-${licenseConditionAddCount}-value`).value = permission;
    }
    document.getElementById(`license-condition-${licenseConditionAddCount}-has-condition`).checked = has_other_condition;

    deleteLicenseCondition();
}

const deleteLicenseCondition = () => {
    const deleteEl = document.querySelectorAll(".license-condition-delete");
    deleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            console.log(tagId)
            document.querySelector(`#${tagId}`).remove();
        }

    });
}


// Limitation
const formatAddLimitation = (action="", permission="", has_other_condition=false) => {
    licenseLimitationAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-4 other-info">
            <select required class="form-select" id="license-limitation-${licenseLimitationAddCount}-key">
            ${limitationSelectOption}
            </select>
        </div>

        <div style="display: inline-block;" class="col-2 other-info">
            <select required class="form-select" id="license-limitation-${licenseLimitationAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>

        <div style="display: inline-block; margin-left: 20px;" class="col-4 other-info">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="license-limitation-${licenseLimitationAddCount}-has-condition">
                <label class="form-check-label" for="gridCheck1">
                    Has condition
                </label>
            </div>
        </div>

        <div style="display: inline-block;" class="col-1 other-info">
            <button type="button" data-tag-id="license-limitation-${licenseLimitationAddCount}" class="btn btn-outline-danger license-limitation-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-limitation-${licenseLimitationAddCount}`);
    divEl.setAttribute('data-tag-id', `license-limitation-${licenseLimitationAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-limitation`);
    divEl.innerHTML = content;
    const containerEl = document.getElementById("license-limitation-container")
    containerEl.appendChild(divEl);


    if(action){
        document.getElementById(`license-limitation-${licenseLimitationAddCount}-key`).value = action;
    }
    if(permission){
        document.getElementById(`license-limitation-${licenseLimitationAddCount}-value`).value = permission;
    }
    document.getElementById(`license-limitation-${licenseLimitationAddCount}-has-condition`).checked = has_other_condition;

    deleteLicenseLimitation();
}

const deleteLicenseLimitation = () => {
    const deleteEl = document.querySelectorAll(".license-limitation-delete");
    deleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            document.querySelector(`#${tagId}`).remove();
        }

    });
}


// Source
const formatAddSource = (action="", permission="") => {
    licenseSourceAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-7 other-info">
            <select required class="form-select" id="license-source-${licenseSourceAddCount}-key">
            ${sourceSelectOption}
            </select>
        </div>

        <div style="display: inline-block;" class="col-3 other-info">
            <select required class="form-select" id="license-source-${licenseSourceAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>
        <div style="display: inline-block;" class="col-1 other-info">
            <button type="button" data-tag-id="license-source-${licenseSourceAddCount}" class="btn btn-outline-danger license-source-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-source-${licenseSourceAddCount}`);
    divEl.setAttribute('data-tag-id', `license-source-${licenseSourceAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-source`);
    divEl.innerHTML = content;
    const containerEl = document.getElementById("license-source-container")
    containerEl.appendChild(divEl);


    if(action){
        document.getElementById(`license-source-${licenseSourceAddCount}-key`).value = action;
    }
    if(permission){
        document.getElementById(`license-source-${licenseSourceAddCount}-value`).value = permission;
    }

    deleteLicenseSource();
}

const deleteLicenseSource = () => {
    const deleteEl = document.querySelectorAll(".license-source-delete");
    deleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            document.querySelector(`#${tagId}`).remove();
        }

    });
}


// Must Include
const formatAddMustInclude = (action="", permission="") => {
    licenseMustIncludeAddCount += 1;
    const divEl = document.createElement('div')
    const content = `
        <div style="display: inline-block;" class="col-7 other-info">
            <select required class="form-select" id="license-must-include-${licenseMustIncludeAddCount}-key">
            ${mustIncludeOption}
            </select>
        </div>

        <div style="display: inline-block;" class="col-3 other-info">
            <select required class="form-select" id="license-must-include-${licenseMustIncludeAddCount}-value">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>
        </div>
        <div style="display: inline-block;" class="col-1 other-info">
            <button type="button" data-tag-id="license-must-include-${licenseMustIncludeAddCount}" class="btn btn-outline-danger license-must-include-delete">X</button>
        </div>
    `

    divEl.setAttribute('id', `license-must-include-${licenseMustIncludeAddCount}`);
    divEl.setAttribute('data-tag-id', `license-must-include-${licenseMustIncludeAddCount}`);
    divEl.setAttribute('class', `col-12 other-info license-must-include`);
    divEl.innerHTML = content;
    const containerEl = document.getElementById("license-must-include-container")
    containerEl.appendChild(divEl);


    if(action){
        document.getElementById(`license-must-include-${licenseMustIncludeAddCount}-key`).value = action;
    }
    if(permission){
        document.getElementById(`license-must-include-${licenseMustIncludeAddCount}-value`).value = permission;
    }

    deleteLicenseMustInclude();
}

const deleteLicenseMustInclude = () => {
    const deleteEl = document.querySelectorAll(".license-must-include-delete");
    deleteEl.forEach(element => {

        element.onclick = function(event){
            const tagId = element.getAttribute("data-tag-id");
            document.querySelector(`#${tagId}`).remove();
        }

    });
}



