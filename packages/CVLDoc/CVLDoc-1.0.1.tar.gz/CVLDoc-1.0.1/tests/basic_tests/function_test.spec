//// #  Function testing.
//// # This function is testing the invoking process
//// # part of the Fahrenheit project

/**
 * @title Callf authorization function.
 * @notice this function is part of the project and
 * performing authorization checks on some addresses.
 * @dev  the function is assuming the declaration  of 'autorizeVoteSigner'
 * function.
 * @param d the first address
 * @param x the unkown signer address
 * @param f the signing function.
 */
function callF(address d, address x, method f) {
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
			calldataarg arg;
			env eF;
			sinvoke f(eF,arg);
	}
}

/**
 * @title getVoterAge - get voter age.
 * @notice this function decides if the sender is old enough to vote
 * it uses the getFullVoterDetails function.
 * @dev  the function is assuming the declaration  of 'getFullVoterDetails'
 * function.
 * @param e the used environment
 * @param voter - the prospect voter address
 * @return the voter age.
 */
function getVoterAge(env e, address voter) returns uint8 {
    uint8 age;
    age, _, _ = getFullVoterDetails(e, voter);
    return age;
}

/**
 * @title getRegistered - get registered.
 * @dev  the function is assuming the declaration  of 'getFullVoterDetails'
 * function.
 * @param e the used environment
 * @param voter - the prospect voter address
 * @return indication if the voter is registered.
 */
 function getRegistered(env e, address voter) returns bool {
    bool isReg;
    _, isReg, _ = getFullVoterDetails(e, voter);
    return isReg;
}
