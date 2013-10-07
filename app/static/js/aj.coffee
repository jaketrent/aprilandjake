#= require components/jquery/jquery
#= require components/fittext/jquery.fittext

$ ->
  $(".home-title").fitText(0.6, { minFontSize: '60px', maxFontSize: '200px' })
  $(".home-subtitle").fitText(1, { minFontSize: '30px', maxFontSize: '80px' })

