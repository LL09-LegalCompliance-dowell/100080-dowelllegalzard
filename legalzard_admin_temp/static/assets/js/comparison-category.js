let license_compared = {};
let eventId = "";
let index = 0;
let updateIndex = 0;
let actionType = "";
document.addEventListener("DOMContentLoaded", function(event){
    
    const formSaveBtnEl = document.querySelector("#btn-save-category-comparison");


    // Display form
    document.getElementById("btn-add-new").onclick = function(event){
        document.querySelector("#category").value = "";
        document.querySelector("#license-1").value = "0";
        document.querySelector("#license-2").value = "0";


        const formEl = document.querySelector("#category-comparison-form");
        formEl.setAttribute("data-method-type", "PUT");
        formEl.setAttribute("data-action-type", "add-license-category-comparison");
        formEl.setAttribute("data-comparison-id", "");
    }



    formSaveBtnEl.onclick = saveDataToDatabase;

    
    loadTable();


})

const saveDataToDatabase = (event) =>{
    event.preventDefault();

    const formEl = document.querySelector("#category-comparison-form");
    const errorContainerEl = document.querySelector("#error-container");
    const errorContentEl = document.querySelector("#error-content");
    const endpoint = formEl.getAttribute("data-endpoint");
    actionType = formEl.getAttribute("data-action-type");
    const comparisonId = formEl.getAttribute("data-comparison-id");
    const category = document.querySelector("#category").value;
    const license1ComparisonValue = document.querySelector("#license-1").value;
    const license2ComparisonValue = document.querySelector("#license-2").value;
    const license1AdditionalInfoValue = document.querySelector("#licensee-1-additional-info").value;
    const license2AdditionalInfoValue = document.querySelector("#licensee-2-additional-info").value;
    const btnSaveData = document.querySelector("#btn-save-category-comparison");


    // reset error 
    errorContainerEl.style.display = "none";
    errorContentEl.textContent = "";

    if (validateInput()){

        // Activate loading
        const loading = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> saving...';
        btnSaveData.innerHTML = loading;
        btnSaveData.disabled = true;


        const data = {
            action_type: actionType,
            comparison_id: comparisonId,
            comparison:{
                category: category,
                licence_1:{
                    name: license_compared.license_1_name,
                    comparison_value: license1ComparisonValue,
                    additional_value: license1AdditionalInfoValue
                },
                licence_2:{
                    name: license_compared.license_2_name,
                    comparison_value: license2ComparisonValue,
                    additional_value: license2AdditionalInfoValue
                }
            }
        }

        fetch(endpoint, {
            method: "PUT",
            body: JSON.stringify(data),
            headers: {"Content-Type": "application/json"}
        }).then(function(response){
            if (response.status === 201 || response.status === 200){

                return response.json();

            }else{


                // set error 
                errorContainerEl.style.display = "block";
                errorContentEl.textContent = "Something went wrong, whilst saving the data!";

                // deactivate loading
                btnSaveData.innerHTML = "Save";
                btnSaveData.disabled = false;


            }

        }).then(function(jsonData){

            const tableBodyEl = document.getElementById("table-body");
            comparison_category = jsonData.comparison;

            index += 1;

            if (actionType === "add-license-category-comparison"){
                const content = tableContent(index, comparison_category);
                tableBodyEl.innerHTML = `${tableBodyEl.innerHTML}${content}`;
            }else{

                const trEl = document.getElementById(`comparison-${comparison_category._id}`)
                const content = tableContentWithOutTR(index, comparison_category, updateIndex);

                const replacement = document.createElement('tr')
                replacement.setAttribute("id", `comparison-${comparison_category._id}`)
                replacement.innerHTML = content;
                trEl.replaceWith(replacement);

            }


            // deactivate loading
            btnSaveData.innerHTML = "Save";
            btnSaveData.disabled = false;
            document.getElementById("btn-close-modal").click();
            listenToEditBtn();


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
    const comparisonEventId = document.getElementById("comparison-category-id").getAttribute("data-comparison-event-id");
    const formEl = document.querySelector("#category-comparison-form");

    const url = "/api/comparisons/"+comparisonEventId+"/";
    formEl.setAttribute("data-endpoint", url);


    fetch(url, {
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

        const data = jsonData.data[0]
        license_compared = data.attributes;
        eventId = data.eventId;



        const tableHeaderLicense1El = document.getElementById("comparison-category-license-1");
        const tableHeaderLicense2El = document.getElementById("comparison-category-license-2");
        const license1LabelModalEl = document.getElementById("license-1-label");
        const license2LabelModalEl = document.getElementById("license-2-label");

        tableHeaderLicense1El.innerHTML = `${license_compared.license_1_name}(${license_compared.license_1_version})`;
        tableHeaderLicense2El.innerHTML = `${license_compared.license_2_name}(${license_compared.license_2_version})`;
        license1LabelModalEl.innerHTML = `${license_compared.license_1_name} <span style="color: red;">*</span>`;
        license2LabelModalEl.innerHTML = `${license_compared.license_2_name} <span style="color: red;">*</span>`;

        for (let comparison_category of license_compared.comparisons){
            index += 1;
            content += tableContent(index, comparison_category);
        }

        tableSpinnerEl.style.display = "none";
        tableBodyEl.innerHTML = content;
        document.getElementById("btn-add-new").style.display = "inline-block";


        listenToEditBtn();
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}

const tableContent = (index, comparison) => {
    const additional_value_1 = comparison.licence_1.additional_value  ? ` - (${comparison.licence_1.additional_value})` : ""
    const additional_value_2 = comparison.licence_2.additional_value  ? ` - (${comparison.licence_1.additional_value})` : ""

    return `
            <tr id="comparison-${comparison._id}">
                  <th scope="row">${index}</th>
                  <td>${comparison.category}</td>
                  <td>${comparison.licence_1.comparison_value}${additional_value_1}</td>
                  <td>${comparison.licence_2.comparison_value}${additional_value_2}</td>
                  <td style="width:10px">

                    <div class="btn-group" role="group" aria-label="action">
                        <a href="#" data-bs-toggle="modal" data-bs-target="#add-and-update-comparison-category" data-id="${comparison._id}"  class="btn btn-primary edit-data">Edit</a>
                    </div>

                  </td>
            </tr>    
            `
}

const tableContentWithOutTR = (index, comparison, updateIndex) => {
    const additional_value_1 = comparison.licence_1.additional_value  ? ` - (${comparison.licence_1.additional_value})` : ""
    const additional_value_2 = comparison.licence_2.additional_value  ? ` - (${comparison.licence_1.additional_value})` : ""
    return `
            
                  <th scope="row">${updateIndex}</th>
                  <td>${comparison.category}</td>
                  <td>${comparison.licence_1.comparison_value}${additional_value_1}</td>
                  <td>${comparison.licence_2.comparison_value}${additional_value_2}</td>
                  <td style="width:10px">

                    <div class="btn-group" role="group" aria-label="action">
                        <a href="#" data-bs-toggle="modal" data-bs-target="#add-and-update-comparison-category" data-id="${comparison._id}"  class="btn btn-primary edit-data">Edit</a>
                    </div>

                  </td>   
            `
}


const listenToEditBtn = () => {
    const editEls = document.querySelectorAll(".edit-data");
    editEls.forEach(function(element){
        element.onclick = function(event){
            const id = this.getAttribute("data-id")
            updateIndex = 0;

            for (let comparison_category of license_compared.comparisons){
                updateIndex += 1;

                if (comparison_category._id === id){
                    
                    const cardFormTitleEl = document.querySelector("#modal-title");
                    const formEl = document.querySelector("#category-comparison-form");
                    formEl.setAttribute("data-method-type", "PUT");
                    formEl.setAttribute("data-action-type", "update-license-category-comparison");
                    formEl.setAttribute("data-comparison-id", id);

                    document.querySelector("#category").value = comparison_category.category;
                    document.querySelector("#license-1").value = comparison_category.licence_1.comparison_value;
                    document.querySelector("#license-2").value = comparison_category.licence_2.comparison_value;
                    document.querySelector("#licensee-1-additional-info").value = comparison_category.licence_2.additional_value;
                    document.querySelector("#licensee-2-additional-info").value = comparison_category.licence_2.additional_value;
                    cardFormTitleEl.textContent = "Update Category Comparison";
                    break;
                }
            }

        }
    })

}


const validateInput = () => {
    let isValid = true;
    const category = document.querySelector("#category").value;
    const license1ComparisonValue = document.querySelector("#license-1").value;
    const license2ComparisonValue = document.querySelector("#license-2").value;
    const license1ErorEl = document.querySelector("#license-1-error");
    const license2ErorEl = document.querySelector("#license-2-error");
    const categoryErorEl = document.querySelector("#category-error");

    if (category === ""){
        isValid = false;
        categoryErorEl.style.display = "block";
    }else{
        categoryErorEl.style.display = "none";
    }

    if (license1ComparisonValue === "0"){
        isValid = false;
        license1ErorEl.style.display = "block";
    }else{
        license1ErorEl.style.display = "none";
    }

    if (license2ComparisonValue === "0"){
        isValid = false;
        license2ErorEl.style.display = "block";
    }else{
        license2ErorEl.style.display = "none";
    }



    return isValid;
}