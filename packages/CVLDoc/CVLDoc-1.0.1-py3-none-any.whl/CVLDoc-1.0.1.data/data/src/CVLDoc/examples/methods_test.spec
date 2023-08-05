//// # methods_test.spec - Natspec testing file for the methods statement.
//// # contains a few declarations of statements.


/**
 * @title mathematical helpe functions.
 * @notice get the  power of 10 n decimal format
 * @dev do not use this function on floating points.
 */
methods {
    get10PowerDecimals(uint8) returns(uint256) envfree
}


/**
 * @title Specification for core ERC20 tokens.
 * @notice contains all ER20 Interface definitions.
 * @dev includes some extended  interfaces that is not implemented yet.
 */
methods {
	balanceOf(address) returns uint256
	transfer(address,uint256) returns bool
	transferFrom(address, address, uint256) returns bool
	approve(address, uint256) returns bool
	allowance(address, address) returns uint256
	totalSupply() returns uint256
	// Extended API - not implemented
	mint(address,uint256) returns bool
	burn(address,uint256)
	owner() returns address
	paused() returns bool
}
