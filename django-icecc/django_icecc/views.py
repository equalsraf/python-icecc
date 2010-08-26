from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from icecc.control import SchedulerControl
from django_icecc.forms import BlockForm

from django_icecc import ICECC_SCHEDULER
__scheduler__ = SchedulerControl(ICECC_SCHEDULER)

def listcs(request):
    """
    List CS hosts
    """
    out = __scheduler__.runall(["listcs", "listblocks"])
    return render_to_response( 'icecc/listcs.html', 
                    {'listcs': out[0], 'blocks' : out[1] }, 
                    context_instance=RequestContext(request) )


def internals(request):
    """
    List internal information from the scheduler, one chunk per host
    """
    out = __scheduler__.internals()
    return render_to_response( 'icecc/internals.html', { 'internals': out }, 
		    context_instance=RequestContext(request) )

def blockcs(request):
    """
    POST target to remove CS hosts
    """

    if request.method != 'POST':
        raise Http404

    form = BlockForm(request.POST)
    if form.is_valid():
        host = form.cleaned_data['host']
        removed = __scheduler__.run("blockcs "+ host)
    else:
        raise Http404

    return render_to_response( 'icecc/blockcs.html', 
		    { 'host' : host, 'removed': removed }, 
		    context_instance=RequestContext(request) )


def listjobs(request):
    """
    List jobs running on the scheduler
    """
    out = __scheduler__.listjobs()
    return render_to_response( 'icecc/listjobs.html', { 'listjobs': out },
		    context_instance=RequestContext(request) )
   

def summary(request):
    """
    Summary view about the scheduler: hosts, version, jobs, commands
    """
    out = __scheduler__.run("help", raw=True)

    return render_to_response( 'icecc/summary.html', 
		    { 'scheduler' : __scheduler__, 'help':out }, 
		    context_instance=RequestContext(request) )

