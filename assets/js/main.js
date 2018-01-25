/**
 * BRUM v1.0.0
 * By Bas, Sander & Tian
 * Copyright (c) 2018 All Rights Reserved.
 * https://github.com/lesander/brum
 */

const cardImages = $(`.card > img`)
const submitBtn = $(`.submit > button`)

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

  $.post(`http://github.brum.ultrahook.com/dawae/${value}`, (response) => {

    // Handle any error(s).
    if (response.statusCode !== 200) {
      alert('Er ging iets mis met het versturen van de keuze. Probeer het nog een keer.')
      console.log(response)
    }

    // TODO: Display the progress screen.
    //       Initialize polling for finished status.
    

  })

})
