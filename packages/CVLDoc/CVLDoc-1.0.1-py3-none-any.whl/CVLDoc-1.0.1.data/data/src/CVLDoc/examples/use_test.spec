/*** use_test.spec  = NatSpec test file for 'use' statement.
 *   some use statements gathere from the testing folder.
 */

/**
  * @title twoParametricRuleInBase
  * @dev  Override the filter of f and Add a filter to g (using an overridden definition)
  */
 use rule twoParametricRuleInBase filtered { f -> isPlusSevenSomeUInt(f),
                                            g -> filterDef(g)
                                          }



