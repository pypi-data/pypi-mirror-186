class JSUtils {
    static isJSONEmpty(json) {
        return json == null || Object.keys(json).length === 0;
    }

    static existsElement(idElement) {
        return document.contains(document.getElementById(idElement))
    }

    static setStyleDisplayById(idElement, styleDisplay) {
        if (this.existsElement(idElement)) {
            document.getElementById(idElement).style.display = styleDisplay
            return true;
        }
        return false;
    }

    static getQueryParameters() {
        return new URLSearchParams(window.location.search);
    }

    static existsElementByQS(selectors) {
        return document.contains(document.querySelector(`${selectors}`))
    }

    static getElementByQS(selectors) {
        return document.querySelector(`${selectors}`)
    }

    /**
     * Remove element from DOM by ID
     * @param elementId
     * @returns {boolean}
     */
    static removeById(elementId) {
        if (this.existsElement(elementId)) {
            document.getElementById(elementId).remove()
            return true;
        }
        return false;
    }

    /**
     *
     * @param tagName HTML Element Tag
     * @param elementId Element ID
     * @param classList List of CSS Classes
     * @param html HTML Content
     * @param idContainer Container ID
     * @param appendToBody Append to body or to container
     */
    static appendChild(tagName, elementId, classList, html, idContainer, appendToBody = false) {
        try {
            let childElement = document.createElement(tagName);
            if (elementId != null) {
                childElement.id = elementId
            }
            if (classList != null) {
                childElement.classList.add(...classList)
            }
            childElement.innerHTML = html
            if (idContainer != null && this.existsElement(idContainer)) {
                document.getElementById(idContainer).appendChild(childElement)
            }
            if (appendToBody && idContainer === null) {
                document.body.appendChild(childElement)
            }
        } catch (e) {
            throw new Error(e)
        }
    }

    static appendChildToExistsElement(element, html) {
        element.innerHTML = html
    }

    static replaceBrowserUrl(newUrl) {
        if (newUrl !== null) {
            window.history.pushState({path: newUrl}, '', newUrl);
        }
    }
}

class DateUtils {
    static date = new Date()

    /**
     * Get a month of year [0-11] and returns -1 if index out of range
     * @param index
     * @returns {number|any}
     */
    static getMonths(index) {
        const monthMap = new Map()
        monthMap.set(0, 'Janeiro');
        monthMap.set(1, 'Fevereiro');
        monthMap.set(2, 'Março');
        monthMap.set(3, 'Abril');
        monthMap.set(4, 'Maio');
        monthMap.set(5, 'Junho');
        monthMap.set(6, 'Julho');
        monthMap.set(7, 'Agosto');
        monthMap.set(8, 'Setembro');
        monthMap.set(9, 'Outubro');
        monthMap.set(10, 'Novembro');
        monthMap.set(11, 'Dezembro');
        return index < 0 || index > monthMap.size ? -1 : monthMap.get(index)
    }

    static getMonthDays(selectors) {
        return DOMUtils.getElementByQS(selectors);
    }

    static getLastDay() {
        return new Date(this.date.getFullYear(), this.date.getMonth() + 1, 0).getMonth()
    }

    static getPrevLastDay() {
        return new Date(this.date.getFullYear(), this.date.getMonth(), 0).getMonth()
    }
}


class AjaxUtils {
    static refresh(idElement) {
        $(`#${idElement}`).load(window.location.href + ` #${idElement}`);
    }

    static refreshContainer() {
        this.refresh('container')
    }

}


class ModalUtils {

    static openModal(idModal) {
        $(`#${idModal}`).modal('show');
    }

    static closeModal(idModal) {
        $(`#${idModal}`).modal('hide');
    }

    static closeAndRemoveModal(idModal, idContainerModal) {
        this.closeModal(idModal);
        JSUtils.removeById(idContainerModal);
    }

    static appendChildModalToBody(idContainerModal, idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName) {
        let divContainerModal = document.createElement('div')
        divContainerModal.id = idContainerModal
        divContainerModal.innerHTML = this.baseContainer(idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName)
        document.body.appendChild(divContainerModal)
    }

    /**
     *
     * @param idModal String
     * @param idForm String
     * @param titleModal String
     * @param modalBody htmlContent
     * @param cancelFuncName functionName();
     * @param confirmFuncName functionName();
     * @returns {string}
     */
    static baseContainer(idModal, idForm, titleModal, modalBody, cancelFuncName, confirmFuncName) {
        return `<div class="modal fade" id="${idModal}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
                    data-focus-on="input:first">
                    <form id="${idForm}" name="${idForm}">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 id="title_modal" class="modal-title">${titleModal === null ? '' : titleModal}</h5>
                                </div>
                                <div class="modal-body">${modalBody}</div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-sm btn-outline-primary" data-bs-toggle="modal" href="#${idModal}"
                                     ${cancelFuncName == null ? '' : 'onclick="' + cancelFuncName + '"'}>Cancelar</button>
                                    <button type="button" class="btn btn-sm btn-primary" onclick="${confirmFuncName}">Confirmar</button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>`
    }
}

class DjangoUtils {
    static getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}

class SpinnerUtils {
    static showSpinner(idSpinner = 'loading', idContainer = 'container') {
        JSUtils.appendChild('div', idSpinner, null, HTMLUtils.getSpinner(), idContainer)
    }

    static hideSpinner(idSpinner = 'loading') {
        JSUtils.removeById(idSpinner)
    }
}

class HTMLUtils {
    static getTimeContainerHtml() {
        return ` <div class="times">`
    }

    static getHtmlModal(json, idModal) {
        return `<!-- Modal -->
            <div class="modal fade" id="${idModal}" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" >${json.title}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" onclick="closeModal()"></button>
                        </div>
                        <div class="modal-body">
                            <!-- Include element with django after apend this element in DOM /-->
                        </div>
                    </div>
                </div>
            </div>`
    }

    static getInputRadio(idElement, value) {
        return `
        <label for="${idElement}">
            <input class="form-check-input" name="inputRadios" id="${idElement}" type="radio">
            <span>${value}</span>
        </label>
        `
    }

    /**
     *
     * @param toastId
     * @param bodyMsg String
     * @param showHeader Boolean
     * @param headerTitle String
     * @param headerMsg String
     * @returns {string} Html
     */
    static getHtmlToast(toastId, bodyMsg, showHeader = false, headerTitle, headerMsg) {
        let _headerHtml = `<div class="toast-header">
                                <strong class="me-auto">${headerTitle}</strong>
                                <small>${headerMsg}</small>
                                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                            </div>`

        return `<div class="toast-container position-fixed bottom-0 end-0 p-3">
                    <div id="${toastId}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                        ${showHeader ? _headerHtml : ''}
                        <div class="toast-body">
                            ${bodyMsg}
                        </div>
                    </div>
                </div>`
    }

    static getSpinner(message = 'loading') {
        return `
            <div class="btn btn-primary position-fixed bottom-0 end-0 p-2 mb-2 me-2" style="cursor: default">
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                ${message}
            </div> `
    }
}

class FetchUtils {
    static fetchHandlerSpinnerGet(url, init, func) {
        init = init || {
            method: 'GET',
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            }
        }
        FetchUtils.fetchHandlerSpinner(url, init, func)
    }

    static fetchHandlerSpinner(url, init, func) {
        SpinnerUtils.showSpinner();

        fetch(url, init)
            .then(json => {
                SpinnerUtils.hideSpinner();
                func(json);
            }).catch(err => {
                SpinnerUtils.hideSpinner();
                console.log(err)
            }
        )
    }

    static fetchHandler(url, init, func) {
        fetch(url, init)
            .then(json => func(json)).catch(err => console.log(err))
    }

    /**
     * addEventListener for element id passed on parameter. After, call a  fetchHandlerGet function.
     * @param elementListenerId element id to add eventListener
     * @param urlPath url path used to concat no queryString
     *
     * ex: If you passed '/blog/', then the complete url was like: http://localhost:8000/blog/?query=xxxxxx
     */
    static eventListenerThenFetchHandlerGet(elementListenerId, urlPath) {
        let search = document.getElementById(elementListenerId)
        search.addEventListener('keypress', (e) => {
            if (e.code === 'Enter') {
                const searchValue = e.target.value;
                const queryString = searchValue === null ? '' : '?query=' + searchValue
                const url = `${urlPath}${queryString}`
                console.log(url)
                FetchUtils.fetchHandlerSpinnerGet(url, null, FetchUtils.afterGetEventListenerThenFetchHandlerGet)
            }
        })
    }

    static afterGetEventListenerThenFetchHandlerGet(json) {
        JSUtils.replaceBrowserUrl(json['url'])
        AjaxUtils.refresh('container');
    }
}