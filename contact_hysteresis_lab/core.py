from .common import number

def run(data):
    samples=data['samples'];low=number(data['release_threshold'],0,1e12);high=number(data['engage_threshold'],low,1e12)
    if low==high or not 1<=len(samples)<=10000:raise ValueError('threshold_or_size')
    on=number(data.get('engage_duration',0),0,1e9);off=number(data.get('release_duration',0),0,1e9);state=data.get('initial_contact',False)
    if not isinstance(state,bool):raise ValueError('state')
    pending=None;events=[];last=-1;raw_events=[];raw_state=state
    for s in samples:
        t=number(s['time'],0,1e12);force=number(s['force'],0,1e12)
        if t<=last:raise ValueError('time_order')
        if pending is not None and pending[0]<=t:
            state=pending[1];events.append({'time':pending[0],'contact':state});pending=None
        raw=force>=high
        if raw!=raw_state:raw_events.append({'time':t,'contact':raw});raw_state=raw
        wanted=True if not state and force>=high else False if state and force<=low else None
        if wanted is None:pending=None
        elif pending is None or pending[1]!=wanted:pending=(t+(on if wanted else off),wanted)
        if pending is not None and pending[0]<=t:
            state=pending[1];events.append({'time':t,'contact':state});pending=None
        last=t
    until=number(data.get('until',last),last,1e12)
    if pending is not None and pending[0]<=until:state=pending[1];events.append({'time':pending[0],'contact':state});pending=None
    return {'contact':state,'events':events,'single_threshold_events':raw_events,'pending':None if pending is None else {'due':pending[0],'contact':pending[1]},'until':until,'assumption':'zero-order hold between samples; crossing at sample timestamps; no unseen inter-sample noise modeled'}
