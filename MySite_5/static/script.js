$("#orderTotal").click(function () {
    calculatePrice();
});
    
function calculatePrice()
{
    //select data
    var adults = 800;
    var kids = 400;
    var teacher = 500;
    var company= 600;
    var institute=700;
    
    var quantityAdults = $("#quantityAdults").val();
    var quantityKids = $("#quantityKids").val();
    var quantityTeacher = $("#quantityTeacher").val();
    var quantityCompany = $("#quantityCompany").val();
    var quantityInstitute =$("#quantityInstitute").val();
    
    //calculate final cost
    
    var total = (quantityAdults * adults) + (quantityKids * kids) + (quantityTeacher *teacher) + (quantityCompany* company) + (quantityInstitute* institute );
    
    console.log(total);
    //print value to orderTotal
    $("#orderTotal").val(total);
}