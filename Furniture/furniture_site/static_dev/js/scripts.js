$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);

    if ($(window).width() > 761) {
        $('.ar-help').removeClass('hidden');
      } else {
        $('.ar-link').removeClass('hidden');
    }

    function cartUpdating(product_id, count, is_delete){
        var data = {};
        data.product_id = product_id;
        data.count = count;
         var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data)
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_count);
                 if (data.products_total_count || data.products_total_count == 0){
                    $('#cart_total_count').text("("+data.products_total_count+")");
                     console.log(data.products);
                     $('.cart-items ul').html("");
                     $.each(data.products, function(k, v){
                        $('.cart-items ul').append('<li>'+ '<div class="cart-elements mt-2"> <span class="title-item">' +
                        v.title +'</span> <span class="count-item">' + v.count + 'шт. </span>' + '<span class="price-item">' +
                        v.price_per_item + '₽ </span>' + '<a class="delete-item" href="" data-product_id="'+ v.id +
                        '"><i class="bi bi-x-lg"></i></a> </div>' +'</li>');
                     });
                 }

             },
             error: function(){
                 console.log("error")
             }
         })

    }

    form.on('submit', function(e){
        e.preventDefault();
        console.log(Number('123'));
        var count = $('#count').val();
        console.log(count);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var title = submit_btn.data("title");
        var price = submit_btn.data("price");
        console.log(product_id);
        console.log(price);
        console.log(title);

        cartUpdating(product_id, count, is_delete=false)

    });

    function showingCart(){
        $('.cart-items').removeClass('hidden');
    };

//    $('.cart-container').on('click', function(e){
//        e.preventDefault();
//        showingBasket();
//    });

    function closeCart(){
        $('.cart-items').addClass('hidden');
     };

     $('.cart-container').mouseover(function(){
         showingCart();
     });

     $('.cart-container').mouseout(function(){
         closeCart();
     });

     $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         product_id = $(this).data("product_id")
         count = 0;
         cartUpdating(product_id, count, is_delete=true)
     });

    function calculatingCartAmount(){
        var total_order_amount = 0;
        $('.total-product-in-cart-amount').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };

    $(document).on('change', ".product-in-cart-count", function(){
        var current_count = $(this).val();
        console.log(current_count);

        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        console.log(current_price);
        var total_amount = parseFloat(current_count*current_price).toFixed(2);
        console.log(total_amount);
        current_tr.find('.total-product-in-cart-amount').text(total_amount);

        calculatingCartAmount();
    });


    calculatingCartAmount();

});