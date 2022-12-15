function initMasks(){
    $(".currency-mask").maskMoney({prefix:'R$ ', allowZero: true, allowNegative: false, thousands:'.', decimal:',', affixesStay: false}).on('change blur', function(){
        $(this).val($(this).val().replace('.', ''))
    })
    $(".currency-mask-with-dot").maskMoney({prefix:'R$ ', allowZero: true, allowNegative: false, thousands:'.', decimal:',', affixesStay: true})
    $(".currency-mask-no-dot").maskMoney({prefix:'R$ ', allowZero: true, allowNegative: false, thousands:'', decimal:',', affixesStay: false})
    $(".currency-mask-without-prefix").maskMoney({allowZero: false, allowNegative: false, thousands:'.', decimal:',', affixesStay: false})
    $('[id^=id_account_plan]').select2()
    $('[id^=id_business_unit]').select2()

    $('.currency-mask-with-dot').each(function() {
        $(this).maskMoney('mask', $(this).val())
    })
}
try {
    initMasks()
}
catch(e){
    console.log('please include maskmoney: http://plentz.github.io/jquery-maskmoney/')
}
