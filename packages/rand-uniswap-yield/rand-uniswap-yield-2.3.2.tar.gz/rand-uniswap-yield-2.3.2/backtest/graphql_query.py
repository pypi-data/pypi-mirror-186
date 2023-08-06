from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import pandas as pd
from datetime import datetime
import time


def create_query(address, fromdate, first_value=1000, skip_value=0):
    first = f"first: {first_value}" if first_value > 0 else ""
    skip = f"skip: {skip_value}" if skip_value > 0 else ""
    # Making the query for gql
    query_text = """
        query ($fromdate: Int!)
        {
            poolHourDatas(
                orderBy:periodStartUnix,
                orderDirection:desc,
                %s,
                %s,
                where:{
                    pool:"%s",
                    periodStartUnix_gt:$fromdate},
            )
        {
            periodStartUnix
            liquidity
            high
            low
            close
            feeGrowthGlobal0X128
            feeGrowthGlobal1X128
            pool {
                totalValueLockedUSD
                totalValueLockedToken1
                totalValueLockedToken0
                token0{ decimals }
                token1{ decimals }
                }
            }
        }
        """ % (
        first,
        skip,
        address,
    )

    query = gql(query_text)
    params = {"fromdate": fromdate}

    return query, params


def get_queried_df(client, address, fromdate_period):
    query, params = create_query(address, fromdate_period)
    result = client.execute(query, variable_values=params)
    return pd.DataFrame(result["poolHourDatas"])


def graph(network: str, address: str, fromdate: int) -> pd.DataFrame:

    if network == "ethereum":
        url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
    elif network == "polygon":
        # 'https://api.thegraph.com/subgraphs/name/steegecs/uniswap-v3-polygon'
        url = "https://api.thegraph.com/subgraphs/name/zephyrys/uniswap-polygon-but-it-works"
    elif network == "arbitrum":
        url = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-arbitrum-one"
    elif network == "optimism":
        url = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-optimism-dev"

    sample_transport = RequestsHTTPTransport(
        url=url,
        verify=True,
        retries=5,
    )
    client = Client(transport=sample_transport)

    # Printing out query date
    fromatted_date = datetime.utcfromtimestamp(fromdate).strftime("%Y-%m-%d %H:%M:%S")
    now_time = datetime.now().timestamp()
    df = pd.DataFrame()
    end_date = fromdate

    # Printing query infos
    print(
        "-------------------------------- GraphQL Query --------------------------------"
    )
    print("Query information:")
    print("Endpoint:", url)
    print("Network:", network)
    print("Pool contract:", address)
    print("Uniswap pool info:", f"https://info.uniswap.org/#/{network}/pools/{address}")
    print("Querying from unix timestamp:", fromdate, "/", fromatted_date)
    print("Querying GraphQL endpoint:", url)

    # Executing query and formatting returned value
    if fromdate > now_time:
        Exception("Warning: fromdate is in the future")
    elif now_time - fromdate < 1000 * 3600:
        print("Query can be done in one request")
        query, params = create_query(address, fromdate, 1000, 0)
        response = client.execute(query, variable_values=params)
        df = pd.json_normalize(response["poolHourDatas"])
    elif now_time - fromdate > 1000 * 3600:
        print("Warning: fromdate is too far in the past, need to query multiple times")
        skip_value = 0
        while True:
            if skip_value >= 5001:  # No more than 5000 skip is allowed on the graph
                print("Warning: skip value is too high, breaking the loop")
                break
            print(f"Queried {df.index.max() - df.index.min()}")
            query, params = create_query(address, fromdate, 1000, skip_value)
            response = client.execute(query, variable_values=params)
            query_df = pd.json_normalize(response["poolHourDatas"])
            if len(query_df) == 0 or query_df["periodStartUnix"].min() < fromdate:
                print("No more data")
                df = df.reset_index(drop=True)
                break
            query_df.set_index(
                pd.to_datetime(query_df.periodStartUnix, unit="s"), inplace=True
            )
            # concatenate dataframes
            df = pd.concat([df, query_df])
            skip_value += 1000
            time.sleep(5)

    else:
        Exception("Warning: error in fromdate: %s - now_time: %s" % fromdate, now_time)

    print("Query succeeded.")
    print(
        "-------------------------------- GraphQL Query --------------------------------"
    )

    df = df.astype(float)

    return df
