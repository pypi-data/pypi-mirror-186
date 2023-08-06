from typing import Any
from typing import Dict
from typing import List

import dict_tools.data as data


async def profiles(
    hub,
    acct_file: str = None,
    acct_key: str = None,
    acct_data: Dict = None,
    **kwargs,
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Read the acct information from the named subs and return the context
    """
    if acct_file and acct_data is None:
        hub.log.debug("Reading profiles from acct")
        acct_data = await hub.acct.init.profiles(acct_file, acct_key, **kwargs)

    if acct_data is None:
        acct_data = {}

    ret_data = data.NamespaceDict()

    for provider, profiles in acct_data.items():
        ret_data[provider] = []
        if not isinstance(profiles, list):
            profiles = [profiles]
        for profile in profiles:
            for name, info in profile.items():
                new_ctx = data.NamespaceDict({name: info})
                ret_data[provider].append(new_ctx)
                if provider in hub.acct:
                    # This profile needs to run through an acct plugin for processing
                    new_info = await hub.acct.init.process(
                        {provider}, {provider: new_ctx}
                    )
                    if new_info[provider]:
                        ret_data[provider].append(data.NamespaceDict({name: new_info}))

    return ret_data
