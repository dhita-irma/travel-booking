$(function () {

    /* ===============================================================
         PRODUCT QUNATITY
      =============================================================== */
      $('.dec-btn').click(function () {
          var siblings = $(this).siblings('input');
          if (parseInt(siblings.val(), 10) >= 1) {
              siblings.val(parseInt(siblings.val(), 10) - 1);
          }
      });

      $('.inc-btn').click(function () {
          var siblings = $(this).siblings('input');
          siblings.val(parseInt(siblings.val(), 10) + 1);
      });


      /* ===============================================================
           BOOTSTRAP SELECT
        =============================================================== */
      $('.selectpicker').on('change', function () {
          $(this).closest('.dropdown').find('.filter-option-inner-inner').addClass('selected');
      });


      /* ===============================================================
           TOGGLE ALTERNATIVE BILLING ADDRESS
        =============================================================== */
      $('#alternateAddressCheckbox').on('change', function () {
         var checkboxId = '#' + $(this).attr('id').replace('Checkbox', '');
         $(checkboxId).toggleClass('d-none');
      });


      /* ===============================================================
           DISABLE UNWORKED ANCHORS
        =============================================================== */
      $('a[href="#"]').on('click', function (e) {
         e.preventDefault();
      });

      /* ===============================================================
           DATE PICKER
        =============================================================== */

        // INITIALIZE DATEPICKER PLUGIN
        $('.datepicker').datepicker({
            clearBtn: true,
            format: "M dd, yyyy"
        });


        // FOR DEMO PURPOSE
        $('#reservationDate').on('change', function () {
            var pickedDate = $('input').val();
            $('#pickedDate').html(pickedDate);
            $('.update-cart').attr('data-date', pickedDate);
        });

        // Activate navbar in all page but index 
        var pathname = window.location.pathname;
        if (pathname != '/') {
            $('.navbar').addClass('active');
        } else {
            // Scroll to toggle transparent navbar on and off
            $(window).on('scroll', function () {
                if ($(window).scrollTop() > 10) {
                    $('.navbar').addClass('active');
                } else {
                    $('.navbar').removeClass('active');
                }
            });
        }
});