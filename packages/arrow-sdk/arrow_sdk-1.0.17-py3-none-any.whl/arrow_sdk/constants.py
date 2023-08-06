from tokenize import Double
from typing import TypedDict
from web3 import Web3

import json
import pkg_resources

def read_abi(path):
    with pkg_resources.resource_stream(__name__, path) as f:
        data = f.read()
        return data

# Provider
w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/avalanche_fuji'))

# Default version
DEFAULT_VERSION = "v4"

# Load contract JSONs
ERC20ABI = json.loads(read_abi('abis/IERC20Metadata.json'))
IArrowRouterABI = json.loads(read_abi('abis/v4/IArrowRouter.json'))
IArrowEventsABI = json.loads(read_abi('abis/v4/IArrowEvents.json'))
IArrowRegistryABI = json.loads(read_abi('abis/v4/IArrowRegistry.json'))
ArrowOptionChainProxyV4ABI = json.loads(read_abi('abis/competition/ArrowOptionChainProxy.json'))
ArrowOptionChainProxyCompetitionABI = json.loads(read_abi('abis/v4/ArrowOptionChainProxy.json'))

# Bytecode
bytecodeHashes = {
    "ArrowOptionChainProxy": {
        "v4": Web3.solidityKeccak(["bytes"], [ArrowOptionChainProxyV4ABI["bytecode"]]),
        "competition": Web3.solidityKeccak(["bytes"], [ArrowOptionChainProxyCompetitionABI["bytecode"]])
    }
}

addresses = {
    "fuji": {
        "router": {
            "v4": "0x752Fe3cC44F785EB1e4A8a6237adAe24184d9979",
            "competition": "0xD05D064DBDCf8dB7D87EcD7E06c63874Bb968AA6"
        }
    }
}

urls = {
    "api": {
        "v4": "https://fuji-v5-api.arrow.markets/v1",
        "competition": "https://competition-v5-api.arrow.markets/v1"
    },
    "provider": {
        "fuji": "https://api.avax-test.network/ext/bc/C/rpc"
    }
}

binanceSymbols = {
    "AVAX": "AVAXUSDT",
    "ETH": "ETHUSDT",
    "BTC": "BTCUSDT"
}

coingeckoIDs = {
    "AVAX": "avalanche-2",
    "ETH": "ethereum",
    "BTC": "bitcoin"
}

versions = {"v4", "competition"}
secondsPerDay = 60 * 60 * 24
quantityScaleFactor = 10**2

class UNSUPPORTED_VERSION_ERROR(Exception):
    """Raised when incorrect version"""
    pass

class UNSUPPORTED_EXPIRATION_ERROR(Exception):
    """Raised when expiration date not Friday"""
    pass

# Custom classes

class Greeks(TypedDict):
    delta: float # Sensitivity of an option’s price to changes in the value of the underlying.
    gamma: float # Change in delta per change in price of the underlying.
    rho: float # Sensitivity of option prices to changes in interest rates.
    theta: float # Measures time decay of price of option.
    vega: float # Change in value from a 1% change in volatility.

class OptionContract(TypedDict):
    ticker: str # Ticker enum that denotes a particular asset.
    expiration: str # Readable expiration date in "MMDDYYYY" format (e.g. "01252022" for January 25th, 2022).
    strike: list # Accepts arrays with two values for spreads. Formatted as [longStrike, shortStrike].
    contractType: int # ContractType enum that indicates whether the option is a call, put, call spread, or put spread.
    price: float # Float number that indicates the price of 1 option.
    spotPrice: float # Most up-to-date price of underlying asset.
    priceHistory: list # Prices of underlying asset over some period of history.
    greeks: Greeks # Greeks interface that specifies which greeks are tied to this option.

class OptionOrderParams(OptionContract):
    quantity: float # Float number of contracts desired in the order.
    orderType: int # OrderType enum that indicates whether this option is a long open, long close, short open, or short close.
    thresholdPrice: float # The minimum (or maximum) price the user is willing to receive (or pay) for this specific option.

class DeliverOptionParams(OptionOrderParams):
    hashedValues: str
    signature: str
    amountToApprove: int
    unixExpiration: int # UTC expiration date of option in UNIX timestamp.
    formattedStrike: str # Turns strike[] into formatted string with format like "longStrike|shortStrike".
    bigNumberStrike: list
    bigNumberThresholdPrice: int

# **********************************
# *          USEFUL TYPES          *
# **********************************

class Version:
    V4 = "v4"
    COMPETITION = "competition"

class ContractType:
    CALL = 0
    PUT = 1
    CALL_SPREAD = 2
    PUT_SPREAD = 3

class OrderType:
    LONG_OPEN = 0
    LONG_CLOSE = 1
    SHORT_OPEN = 2
    SHORT_CLOSE = 3

