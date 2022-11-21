export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    /* cantidad captadora */
    get amount() {
        return this._amount;
    }

    /* monto fijador */
    set amount(value) {
        this._amount = value;
    }

    /* captador de moneda */
    get currency() {
        return this._currency;
    }

    /* setter moneda */
    set currency(value) {
        this._currency = value;
    }

    displayFullPrice() {
        const currencyAll = this._currency.displayFullCurrency();
        return `${this._amount} ${currencyAll}`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}
