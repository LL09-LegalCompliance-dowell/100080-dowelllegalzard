let index = 0;
let updateIndex = 0;
let fileData = {};
let licenseTagAddCount = 0;

document.addEventListener("DOMContentLoaded", function(event){

    getLicenseCount();
    getLicenseComparisonCount();


})


const getLicenseCount = () => {
   
    const spinnerEl = document.getElementById("licenses-count-spinner");
    const licensesCountEl = document.getElementById("licenses-count");
    const countContainerEl = document.getElementById("licenses-count-container");
    

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

        licensesCountEl.textContent = jsonData.data.length;
        spinnerEl.style.display = "none";
        countContainerEl.style.display = "block";
        countContainerEl.setAttribute("class", "d-flex align-items-center")
        

    }).catch(function(err){
        spinnerEl.style.display = "none";

    })


    

}


const getLicenseComparisonCount = () => {
   
    const spinnerEl = document.getElementById("license-comparison-spinner");
    const comparisonCountEl = document.getElementById("comparison-count");
    const countContainerEl = document.getElementById("comparison-count-container");
    

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

        comparisonCountEl.textContent = jsonData.data.length;
        countContainerEl.style.display = "block";
        spinnerEl.style.display = "none";
        countContainerEl.setAttribute("class", "d-flex align-items-center")

    
    }).catch(function(err){
        spinnerEl.style.display = "none";

    })

}



