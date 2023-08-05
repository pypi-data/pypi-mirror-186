/***
    # testing  NatSpec file for invariants contains all sort of invariants.
    # each invariant has a somewhat different tags associated with it.
*/

/**
 * @title totalSupply_LE_balance
 * @notice invariant to assure that the total supply is always under the balance amount.
 *  the variant has no parameters.
 * @dev assume currentContract is initiated.
 */
invariant totalSupply_LE_balance()
    totalSupply() <= underlying.balanceOf(currentContract)
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
        }
    }

/**
 * @title totalSupply_vs_balance
 * @notice The total supply of the system si zero if and only if the balanceof the system is zero
 * the variant has no parameters
*/
invariant totalSupply_vs_balance()
    totalSupply() == 0 <=> underlying.balanceOf(currentContract) == 0
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
        }
    }

/**
 * @title proxyNotZero
 * @notice make sure that the proxy is not zero.
 * @dev make use of 'getOrCreateProxy'
 * @param a = proxy address
*/
invariant proxyNotZero(address a) getOrCreateProxy(a) != 0

/**
 * @title check - check all addresses.
 * @dev make use of 'getVoteSigner' and 'isAccount'
 * @param x = source address
 * @param d = destination address
*/
invariant check(address x, address d)
		!sinvoke isAccount(x) && sinvoke getVoteSigner(x)==d  => d==0
