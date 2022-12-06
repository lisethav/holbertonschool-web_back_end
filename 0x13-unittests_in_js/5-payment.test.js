'use strict';
const sinon = require('sinon');
const chai = require('chai');

const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi function', () => {
  let spyConsole;
  beforeEach(() => spyConsole = sinon.spy(console, 'log'));
  afterEach(() => spyConsole.restore());

  it('sendPaymentRequestToAPI(100, 20)', () => {
    sendPaymentRequestToApi(100, 20);
    chai.expect(spyConsole.calledWith('The total is: 120')).to.be.true;
    chai.expect(spyConsole.calledOnce).to.be.true;
  });
  it('sendPaymentRequestToAPI(10, 10)', () => {
    sendPaymentRequestToApi(10, 10);
    chai.expect(spyConsole.calledWith('The total is: 20')).to.be.true;
    chai.expect(spyConsole.calledOnce).to.be.true;
  });
});
