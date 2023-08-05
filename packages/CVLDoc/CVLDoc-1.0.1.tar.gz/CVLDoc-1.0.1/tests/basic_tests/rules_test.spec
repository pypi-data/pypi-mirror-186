/*** # Natspec for rules.
 * ## A testing file for rules definitions comments.
 * ## it contains rules with and without parameters
 ***/

/**
  * @title Simple rule for checking authorizations
  * @notice  getting two addresses and a method.
  * checking if the sender is autorise to run the method.
  * @dev Note: this is a parametric rule.
  * @param d - the address of the sender
  * @param x - the address of the function invoker
  * @param f - the function to be invoked.
  **/
rule simple(address d, address x, method f) {

	env eF;
	calldataarg arg;
	if (!f.isFallback && f.selector ==  authorizeVoteSigner(address).selector) {
	       require (eF.msg.sender == x);
           sinvoke authorizeVoteSigner(eF,d);
	}
	else {
				sinvoke f(eF,arg);
	}
	assert false;

}

/** # simple2 - another simple rule.
  * @title Selector rule.
  * @dev this rule is testing the sinvoke function.
  * @param d the address of the sender.
  * @param x the address of the receiver
  * @param ff - this doesn't exist.
  **/
rule simple2(address d, address x, method f) {
	calldataarg arg;
	if (!f.isFallback && f.selector ==  authorizeVoteSigner(address).selector) {
	       env eF;
		   require (eF.msg.sender == x);
           sinvoke authorizeVoteSigner(eF,d);
	}
	else if(!f.isFallback && f.selector == createAccount().selector) {
		env eF;
		sinvoke createAccount(eF);
	}
	else {
			env eF;
			sinvoke f(eF,arg);
	}
	assert false;
}

/**
  * @title simple3 - another simple rule.
  * @notice this is a very short and simple rule
  * @dev this rule is testing the sinvoke function.
  * @param d the first address.
  * @param x the second address.
  * @param f - the method that is being tested.
  **/
rule simple3(address d, address x, method f) {
	callF(d,x,f);
	assert false;
}
