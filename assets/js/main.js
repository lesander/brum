const cardImages = $(`.card > img`)
const submitBtn = $(`.submit > button`)

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

$(submitBtn).on(`click`, (event) => {

  const value = $(`.card.selected`).attr(`data-location`)
  $.post(`http://github.brum.ultrahook.com/dawae/${value}`, (response) => {
    console.log(response)
  })

  // TODO: Display progress screen.
  //       Initialize polling for finish.
})
