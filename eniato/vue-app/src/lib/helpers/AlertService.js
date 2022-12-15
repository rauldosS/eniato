import Swal from 'sweetalert2'

export default class AlertService {
  static alert = (attributes) => {
    const options = {
      buttonsStyling: false,
      customClass: {
        confirmButton: 'button primary-button mr-1 ml-1',
        cancelButton: 'button highlight-button mr-1 ml-1',
        header: 'pt-2',
        title: 'text-dark'
      },
      showCloseButton: false,
      ...attributes
    }
    return Swal.fire(options)
  }

  static info = (options) => {
    return AlertService.alert({
      width: 600,
      ...options
    })
  }

  static error = ({
    text = 'Ocorreu um erro de conexão com os nossos servidores. Nossa equipe de desenvolvimento já foi notificada e está trabalhando para resolver o problema.',
    showConfirmButton = false,
    padding = '3.5em',
    title = 'Falha Interna no Servidor'
  }) => {
    return AlertService.alert({
      title,
      text: text,
      showConfirmButton: showConfirmButton,
      width: 600,
      padding: padding
    })
  }

  static internalError = prependText => {
    const appendText = 'Tente novamente ou entre em contato com a equipe de desenvolvimento.'
    const text = prependText ? `${prependText} ${appendText}` : appendText
    return AlertService.error({ text, showConfirmButton: true, padding: '1em' })
  }

  static deleteConfirmation = (options) => {
    return AlertService.alert({
      showCancelButton: true,
      cancelButtonColor: '#d33',
      ...options
    })
  }

  static dialogConfirmation = (options) => {
    return AlertService.alert({
      showCancelButton: true,
      ...options
    })
  }

  static deleteConfirmationWithReason = (options) => {
    return AlertService.alert({
      showCancelButton: true,
      cancelButtonColor: '#d33',
      input: 'text',
      inputAttributes: {
        autocapitalize: 'off'
      },
      ...options
    })
  }

  static successNotification = (title, text) => {
    return AlertService.alert({
      title,
      text
    })
  }

  static notAvailable = ({ text }) => {
    return AlertService.alert({
      title: 'Conteúdo Indisponível',
      text: text,
      showConfirmButton: false,
      width: 600,
      padding: '3.5em'
    })
  }

  static timedError (message) {
    return Swal.fire({
      position: 'bottom-end',
      title: message,
      showConfirmButton: false,
      timer: 1500
    })
  }

  static listedErrors = (errorList, title) => {
    const errorDict = {}
    let errorMsg = '<ul style="padding-top: 10px">'

    errorList.forEach(error => {
      const message = `<li style="padding-top: 5px;">${error.message}</li>`
      if (!Object.keys(errorDict).includes(error.row.toString())) {
        errorDict[error.row] = [message]
      } else {
        errorDict[error.row].push(message)
      }
    })

    Object.keys(errorDict).forEach(key => {
      errorMsg += `
      <li> 
        Linha ${key}
        <ul style="font-size: .9rem">
          ${errorDict[key].join('')}
        </ul>
      </li>
      `
    })

    errorMsg += '</ul>'

    return AlertService.alert({
      title,
      html: errorMsg,
      showConfirmButton: true,
      width: 700,
      padding: '1.5em',
      customClass: {
        content: 'text-left',
        confirmButton: 'button primary-button ml-1 mr-1',
        cancelButton: 'button highlight-button ml-1 mr-1',
        header: 'pt-2',
        title: 'text-dark'
      }
    })
  }
}
