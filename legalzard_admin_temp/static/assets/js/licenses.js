let index = 0;
let updateIndex = 0;

document.addEventListener("DOMContentLoaded", function(event){

    // const btnSaveEl = document.querySelector("#btn-save-license-comparison");


    // Display form
    // document.getElementById("btn-add-new").onclick = function(event){
    //     document.querySelector("#license-1").value = "0";
    //     document.querySelector("#license-2").value = "0";


    //     const formEl = document.querySelector("#license-comparison-form");
    //     formEl.setAttribute("data-method-type", "POST");
    //     formEl.setAttribute("data-endpoint", "/api/comparisons/");
    //     // formEl.setAttribute("data-comparison-id", "");
    // }


    // btnSaveEl.onclick = saveDataToDatabase;

    // loadLicenseDropdown();
    loadTable();


})

const saveDataToDatabase = (event) =>{
    event.preventDefault();

    const formEl = document.querySelector("#license-comparison-form");
    const errorContainerEl = document.querySelector("#error-container");
    const errorContentEl = document.querySelector("#error-content");
    const endpoint = formEl.getAttribute("data-endpoint");
    const methodType = formEl.getAttribute("data-method-type");
    const license1EventId = document.querySelector("#license-1").value;
    const license2EventId = document.querySelector("#license-2").value;
    const btnSaveData = document.querySelector("#btn-save-license-comparison");


    // reset error 
    errorContainerEl.style.display = "none";
    errorContentEl.textContent = "";

    if (validateInput()){

        // Activate loading
        const loading = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> saving...';
        btnSaveData.innerHTML = loading;
        btnSaveData.disabled = true;


        const data = {
            license_1_event_id: license1EventId,
            license_2_event_id: license2EventId
        }


        fetch(endpoint, {
            method: methodType,
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

            index += 1;

            if (methodType === "POST"){

                const content = tableContent(index, jsonData.data[0]);
                tableBodyEl.innerHTML = `${tableBodyEl.innerHTML}${content}`;

            }else{

                // const trEl = document.getElementById(`comparison-${comparison_category._id}`)
                // const content = tableContentWithOutTR(index, comparison_category, updateIndex);

                // const replacement = document.createElement('tr')
                // replacement.setAttribute("id", `comparison-${comparison_category._id}`)
                // replacement.innerHTML = content;
                // trEl.replaceWith(replacement);

            }


            // deactivate loading
            btnSaveData.innerHTML = "Save";
            btnSaveData.disabled = false;
            document.getElementById("btn-close-modal").click();
            // listenToEditBtn();


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
                        <a href="/api/licenses/${data.eventId}/" data-id="${data.eventId}"  class="btn btn-primary">Edit</a>
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

            // load provider for update
            fetch(`/provider/${id}`,{
                method:"GET",
                headers: {"Content-Type": "application/jsons"}
            }).then(function(response){
                if (response.status === 200){
                    return response.json();
                }
            }).then(function(jsonData){

                const formContainerEl = document.querySelector("#form-container");
                const providerNameEl = document.querySelector("#provider-name");
                const cardFormTitleEl = document.querySelector("#card-form-title");
                const formEl = document.querySelector("#form");
                document.querySelector("#provider-name").value = jsonData.name;

                formContainerEl.style.display = "block";
                cardFormTitleEl.textContent = "Update Provider";
                providerNameEl.textContent = "";
                formEl.setAttribute("data-method-type", "PUT");
                formEl.setAttribute("data-endpoint", `/provider/${id}`);

            })

        }
    })

}


const validateInput = () => {
    let isValid = true;
    const license1 = document.querySelector("#license-1").value;
    const license2 = document.querySelector("#license-2").value;
    const license1ErorEl = document.querySelector("#license-1-error");
    const license2ErorEl = document.querySelector("#license-2-error");

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



    return isValid;
}