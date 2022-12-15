(function(){
    function adjust_billing_card_size(el) {
        var requests = $(el);
        var row = requests.find('.stages.row');
        var height = row.height();
        requests.find('li>div.card').height(
            requests.hasClass('opened') ? height : ''
        );
    }

    $('[id^=client-]').click(function(){
        var client_div = $(this);
        if (window.location.pathname.indexOf('archived') == -1){
            var href = $(client_div.find('[id^=client-detail-url-]')[0]).attr('href');
        } else {
            var href = $(client_div.find('[id^=client-archived-detail-url-]')[0]).attr('href');
        }
        window.location = href;
    });

    var btns = $('[id^=billing-]').find('.btn.open-billing');

    btns.click(function (e){
        e.stopPropagation();
        var btn = $(this);
        var billing = btn.parents().closest('[id^=billing-]');
        billing.toggleClass('opened');
        adjust_billing_card_size(billing);
    });

    btns.parents().closest('div.card-body').click(function (e){
        e.stopPropagation();
        var btn = $(this);
        var billing = btn.parents().closest('[id^=billing-]').not('.opened');
        billing.toggleClass('opened');
        adjust_billing_card_size(billing);
    });

    $('[data-toggle="tooltip"]').tooltip({'placement': 'right'});
})();
