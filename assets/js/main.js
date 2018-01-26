/**
 * BRUM v1.0.0
 * By Bas, Sander & Tian
 * Copyright (c) 2018 All Rights Reserved.
 * https://github.com/lesander/brum
 */

const cardImages = $(`.card > img`)
const submitBtn = $(`.submit > button`)
const endpoint = `http://188.166.124.168`

/**
 * Select or deselect the clicked card on click
 *  and enable or disable the submit button.
 * @param  {Element} cardImages
 * @return {void}
 */
$(cardImages).on(`click`, (event) => {

  const card = $(event.target).parent()

  const wasSelected = $(card).hasClass(`selected`)
  $(`.card`).removeClass(`selected`)
  $(submitBtn).attr(`disabled`, true)

  if (!wasSelected) {
    $(card).addClass(`selected`)
    $(submitBtn).removeAttr(`disabled`)
  }

})

/**
 * Submit the chosen destination on click of the submit button.
 * @param  {Element} submitBtn
 * @return {void}
 */
$(submitBtn).on(`click`, (event) => {

  const value = $(`.card.selected`).attr(`data-location`)

  $.post(`${endpoint}/destination/${value}`, (response) => {

    // Handle any error(s).
    if (response.statusCode !== 200) {
      alert('Er ging iets mis met het versturen van de keuze. Probeer het nog een keer.')
      console.log(response)
    }

    // Display the in-transit screen.
    $(`#buttons`).hide()
    $(`#status`).show()

    // Start polling for the finished status every five seconds.
    // Once BRUM has arrived, we stop the interval and show the
    // user the arrived screen.
    const polling = setInterval(() => {

      if (!hasArrived) {
        $.post(`${endpoint}/status`, (response) => {
          if (response.body == 'arrived') {
            clearInterval(polling)
            $(`#status > .in-transit`).hide()
            $(`#status > .arrived`).show()
          }
        })
      }

    }, 5000)

  })

})
