from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm

# Placeholder content for the services showcase section.
SERVICES = [
    {
        'icon': '🏗️',
        'title': 'Commercial Construction',
        'description': (
            'Ground-up construction and tenant improvements for offices, '
            'retail spaces, and industrial facilities, delivered on time '
            'and on budget.'
        ),
    },
    {
        'icon': '🏠',
        'title': 'Residential Building',
        'description': (
            'Custom homes and multi-family developments built with '
            'quality materials and meticulous attention to detail.'
        ),
    },
    {
        'icon': '🔨',
        'title': 'Renovation & Remodeling',
        'description': (
            'Kitchen, bathroom, and whole-home renovations that modernize '
            'your space while respecting your budget and timeline.'
        ),
    },
    {
        'icon': '📐',
        'title': 'Design & Planning',
        'description': (
            'In-house architectural planning and project management to '
            'take your vision from concept to blueprint to reality.'
        ),
    },
]

# Placeholder content for the recent projects showcase.
PROJECTS = [
    {
        'title': 'Riverside Office Park',
        'category': 'Commercial',
        'image': 'images/project-placeholder-1.jpg',
        'description': '45,000 sq. ft. Class A office campus completed in 14 months.',
    },
    {
        'title': 'Maple Grove Residences',
        'category': 'Residential',
        'image': 'images/project-placeholder-2.jpg',
        'description': '32-unit modern townhome community with sustainable design.',
    },
    {
        'title': 'Downtown Lofts Renovation',
        'category': 'Renovation',
        'image': 'images/project-placeholder-3.jpg',
        'description': 'Historic warehouse converted into 18 luxury loft apartments.',
    },
]

# Placeholder client testimonials.
TESTIMONIALS = [
    {
        'quote': (
            'Falcon Builders delivered our office build-out ahead of '
            'schedule and under budget. Their communication throughout '
            'the project was outstanding.'
        ),
        'name': 'Sarah Whitman',
        'role': 'COO, Meridian Logistics',
    },
    {
        'quote': (
            'From the first walkthrough to the final punch list, the '
            'Falcon team treated our home like it was their own. '
            'Highly recommended.'
        ),
        'name': 'James & Priya Anand',
        'role': 'Homeowners, Maple Grove',
    },
    {
        'quote': (
            'Professional, responsive, and genuinely skilled. Our '
            'renovation was the smoothest construction project we have '
            'ever managed.'
        ),
        'name': 'David Chen',
        'role': 'Property Manager, Downtown Lofts',
    },
]

# Certifications / trust badges (placeholder).
CERTIFICATIONS = [
    'Licensed General Contractor',
    'OSHA 30-Hour Certified',
    'A+ Better Business Bureau Rating',
    'LEED Accredited Professionals on Staff',
]

STATS = [
    {'value': '22+', 'label': 'Years in Business'},
    {'value': '350+', 'label': 'Projects Completed'},
    {'value': '98%', 'label': 'Client Satisfaction'},
    {'value': '40+', 'label': 'Skilled Tradespeople'},
]

# Full portfolio for the dedicated Projects page (more entries + metadata
# than the 3-item home page teaser above).
PORTFOLIO = [
    {
        'title': 'Riverside Office Park',
        'category': 'commercial',
        'category_label': 'Commercial',
        'location': 'Springfield, ST',
        'year': '2025',
        'description': '45,000 sq. ft. Class A office campus completed in 14 months, featuring a full glass curtain wall and LEED Silver certification.',
        'variant': 1,
    },
    {
        'title': 'Maple Grove Residences',
        'category': 'residential',
        'category_label': 'Residential',
        'location': 'Maple Grove, ST',
        'year': '2024',
        'description': '32-unit modern townhome community with sustainable design, shared green space, and energy-efficient building envelopes.',
        'variant': 2,
    },
    {
        'title': 'Downtown Lofts Renovation',
        'category': 'renovation',
        'category_label': 'Renovation',
        'location': 'Downtown Springfield, ST',
        'year': '2024',
        'description': 'Historic 1920s warehouse converted into 18 luxury loft apartments while preserving original brick and timber framing.',
        'variant': 3,
    },
    {
        'title': 'Northgate Retail Plaza',
        'category': 'commercial',
        'category_label': 'Commercial',
        'location': 'Northgate, ST',
        'year': '2023',
        'description': '60,000 sq. ft. mixed-use retail plaza with anchor tenant build-out, surface parking, and coordinated site utilities.',
        'variant': 4,
    },
    {
        'title': 'Hillcrest Custom Home',
        'category': 'residential',
        'category_label': 'Residential',
        'location': 'Hillcrest, ST',
        'year': '2023',
        'description': 'Ground-up 4,200 sq. ft. custom single-family residence with an open-concept layout and integrated smart-home wiring.',
        'variant': 5,
    },
    {
        'title': 'Union Street Kitchen Remodel',
        'category': 'renovation',
        'category_label': 'Renovation',
        'location': 'Union Street, ST',
        'year': '2023',
        'description': 'Full gut renovation of a residential kitchen and adjoining dining space, completed in six weeks with zero change orders.',
        'variant': 6,
    },
    {
        'title': 'Cedar Valley Distribution Center',
        'category': 'commercial',
        'category_label': 'Commercial',
        'location': 'Cedar Valley, ST',
        'year': '2022',
        'description': '120,000 sq. ft. logistics and distribution facility with reinforced loading docks and high-bay racking clearance.',
        'variant': 7,
    },
    {
        'title': 'Willow Creek Townhomes',
        'category': 'residential',
        'category_label': 'Residential',
        'location': 'Willow Creek, ST',
        'year': '2022',
        'description': '12-unit townhome development delivered in three phases, each finished ahead of its scheduled completion date.',
        'variant': 8,
    },
    {
        'title': 'Heritage Bank Branch Remodel',
        'category': 'renovation',
        'category_label': 'Renovation',
        'location': 'Downtown Springfield, ST',
        'year': '2022',
        'description': 'Interior renovation of a working bank branch, phased after hours to keep the location open during business hours.',
        'variant': 9,
    },
]


def home(request):
    """Home page view: renders hero, overview, services, projects,
    trust signals, and handles the contact form submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out! A Falcon Builders project "
                "manager will contact you within one business day."
            )
            return redirect('core:home')
    else:
        form = ContactForm()

    context = {
        'services': SERVICES,
        'projects': PROJECTS,
        'testimonials': TESTIMONIALS,
        'certifications': CERTIFICATIONS,
        'stats': STATS,
        'form': form,
    }
    return render(request, 'core/home.html', context)


def contact(request):
    """Dedicated contact page: recommended contact channels alongside a
    lightweight, JS-driven contact form ready to wire up to an email
    service or API endpoint."""
    return render(request, 'core/contact.html')


def projects(request):
    """Dedicated Projects/Portfolio page. Category filtering and the
    scroll-triggered fade-in morph reveal are handled client-side."""
    context = {'portfolio': PORTFOLIO}
    return render(request, 'core/projects.html', context)
