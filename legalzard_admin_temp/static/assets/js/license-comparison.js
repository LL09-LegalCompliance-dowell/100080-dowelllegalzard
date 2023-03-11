let index = 0;
let updateIndex = 0;
let license_compared_data_list = [];
let responseStatus = 400;

document.addEventListener("DOMContentLoaded", function(event){

    const btnSaveEl = document.querySelector("#btn-save-license-comparison");


    // Display form
    document.getElementById("btn-add-new").onclick = function(event){
        document.querySelector("#license-1").value = "0";
        document.querySelector("#license-2").value = "0";


        const formEl = document.querySelector("#license-comparison-form");
        formEl.setAttribute("data-method-type", "POST");
        formEl.setAttribute("data-action-type", "");
        formEl.setAttribute("data-endpoint", "/api/comparisons/");
    }


    btnSaveEl.onclick = saveDataToDatabase;

    loadLicenseDropdown();
    loadTable();


})

const saveDataToDatabase = (event) =>{
    event.preventDefault();

    const formEl = document.querySelector("#license-comparison-form");
    const errorContainerEl = document.querySelector("#error-container");
    const errorContentEl = document.querySelector("#error-content");
    const endpoint = formEl.getAttribute("data-endpoint");
    const methodType = formEl.getAttribute("data-method-type");
    const actionType = formEl.getAttribute("data-action-type");
    const license1EventId = document.querySelector("#license-1").value;
    const license2EventId = document.querySelector("#license-2").value;
    const percentageOfCompatibility = document.querySelector("#percentage-of-compatibility").value;
    const recommendation = document.querySelector("#recommendation").value;
    const recommendationDetails = document.querySelector("#recommendation-details").value;
    const disclaimer = document.querySelector("#disclaimer").value;
    const btnSaveData = document.querySelector("#btn-save-license-comparison");


    // reset error 
    errorContainerEl.style.display = "none";
    errorContentEl.textContent = "";

    if (validateInput()){

        // Activate loading
        const loading = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> saving...';
        btnSaveData.innerHTML = loading;
        btnSaveData.disabled = true;
        responseStatus = 400;


        const data = {
            action_type: actionType,
            license_1_event_id: license1EventId,
            license_2_event_id: license2EventId,
            percentage_of_compatibility: percentageOfCompatibility,
            recommendation: sanitizeText(recommendation),
            recommendation_details: sanitizeText(recommendationDetails),
            disclaimer: sanitizeText(disclaimer),
        }

        console.log(data)

        fetch(endpoint, {
            method: methodType,
            body: JSON.stringify(data),
            headers: {"Content-Type": "application/json"}
        }).then(function(response){
            return response.json();

        }).then(function(jsonData){


            // check for error
            if (jsonData.status_code === 201 || jsonData.status_code === 200){

                const tableBodyEl = document.getElementById("table-body");
                index += 1;
    
                if (methodType === "POST"){
    
                    const content = tableContent(index, jsonData.data[0]);
                    tableBodyEl.innerHTML = `${tableBodyEl.innerHTML}${content}`;
    
                }else{
                    window.location.reload();
                }
    
    
                // deactivate loading
                btnSaveData.innerHTML = "Save";
                btnSaveData.disabled = false;
                document.getElementById("btn-close-modal").click();
                listenToEditBtn();
    

            }else{
                console.log("me to")
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

    fetch("/api/comparisons/", {
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
        license_compared_data_list = jsonData.data;

        for (let license_compared of license_compared_data_list){
            index += 1;
            content += tableContent(index, license_compared);
        }

        tableSpinnerEl.style.display = "none";
        tableBodyEl.innerHTML = content;
        document.getElementById("btn-add-new").style.display = "inline-block";
        listenToEditBtn();
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}


const loadLicenseDropdown = () => {
   
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

    
        let content = '<option  selected disabled value="0">--please choose--</option>';
        const licence1El = document.getElementById("license-1");
        const licence2El = document.getElementById("license-2");

        for (let license of jsonData.data){
            content += `<option value="${license.eventId}">${license.softwarelicense.license_name}(${license.softwarelicense.version})</option>`;
        }

        licence1El.innerHTML = content;
        licence2El.innerHTML = content;
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}

const tableContent = (index, license_compared) => {
    compared = license_compared["attributes"]
    return `
            <tr>
                  <th scope="row">${index}</th>
                  <td>
                      ${compared.license_1_name}(${compared.license_1_version})&nbsp;&nbsp;&nbsp;vs&nbsp;&nbsp;&nbsp;
                      ${compared.license_2_name}(${compared.license_2_version})</td>
                  <td>
                      <img src="${compared.license_1_logo_url}" height="50px" alt="${compared.license_1_name}">
                      &nbsp;&nbsp;&nbsp;vs&nbsp;&nbsp;&nbsp;
                      <img src="${compared.license_2_logo_url}" height="50px" alt="${compared.license_2_name}">
                  </td>
                  <td style="width: 20px">

                    <div class="btn-group" role="group" aria-label="action">
                        <a target="_blank" href="/temp-admin/comparison-categories/${license_compared.eventId}/" data-id="${license_compared.eventId}"  class="btn btn-secondary">view category</a>
                        <a href="#" data-bs-toggle="modal" data-bs-target="#add-and-update-license-comparison" data-id="${license_compared.eventId}"  class="btn btn-primary edit-data">Edit</a>
                    </div>

                  </td>
            </tr>    
            `
}


const listenToEditBtn = () => {
    const editEls = document.querySelectorAll(".edit-data");
    editEls.forEach(function(element){
        element.onclick = function(event){
            const id = this.getAttribute("data-id")
            updateIndex = 0;

            for (let license_compared of license_compared_data_list){
                updateIndex += 1;

                if (license_compared.eventId === id){
                    const data = license_compared['attributes'];
                    const cardFormTitleEl = document.querySelector("#modal-title");
                    const formEl = document.querySelector("#license-comparison-form");
                    formEl.setAttribute("data-method-type", "PUT");
                    formEl.setAttribute("data-action-type", "update-license-comparison");
                    formEl.setAttribute("data-event-id", license_compared.eventId);
                    const url = "/api/comparisons/"+license_compared.eventId+"/";
                    formEl.setAttribute("data-endpoint", url);

                    
                    document.querySelector("#license-1").value = data.license_1_event_id;
                    document.querySelector("#license-2").value = data.license_2_event_id;
                    document.querySelector("#percentage-of-compatibility").value = data.percentage_of_compatibility;
                    document.querySelector("#recommendation").value = data.recommendation;
                    document.querySelector("#recommendation-details").value = data.recommendation_details;
                    document.querySelector("#disclaimer").value = data.disclaimer;
                    cardFormTitleEl.textContent = "Update License Compare";
                    break;
                }
            }

        }
    })

}


const validateInput = () => {
    let isValid = true;
    const license1 = document.querySelector("#license-1").value;
    const license2 = document.querySelector("#license-2").value;
    const percentageOfCompatibility = document.querySelector("#percentage-of-compatibility").value;
    const license1ErorEl = document.querySelector("#license-1-error");
    const license2ErorEl = document.querySelector("#license-2-error");
    const percentageOfCompatibilityErrorErorEl = document.querySelector("#percentage-of-compatibility-error");

    if (license1 === "0"){
        isValid = false;
        license1ErorEl.style.display = "block";
    }else{
        license1ErorEl.style.display = "none";
    }

    if (license2 === "0"){
        isValid = false;
        license2ErorEl.style.display = "block";
    }else{
        license2ErorEl.style.display = "none";
    }

    if (percentageOfCompatibility === "0" || percentageOfCompatibility === ""){
        isValid = false;
        percentageOfCompatibilityErrorErorEl.style.display = "block";
    }else{
        percentageOfCompatibilityErrorErorEl.style.display = "none";
    }



    return isValid;
}


const sanitizeText = (text) => {
    return text.replace(/["${}]/g,"");
}
