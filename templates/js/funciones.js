$(function() {
    $( ".datePicker" ).datepicker({
        dateFormat: "dd/mm/yy",
        showOn: "button",
        buttonImage: "images/calendar.gif",
        buttonImageOnly: true
    });
    
    $( "#dialog-message" ).dialog({
			modal: true,
			autoOpen: false,
			buttons: {
				Ok: function() {
					$( this ).dialog( "close" );
				}
			}
		});
    
    $('.open-mensaje').click(function()
    {
        $('#dialog-message').dialog('open');
        return false;
    })
});

