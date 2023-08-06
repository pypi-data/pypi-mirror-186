import datetime
import calendar
import click
import requests


from cgc.commands.billing.billing_utils import (
    print_billing_status,
    print_compute_stop_events,
    print_volume_stop_events,
)
from cgc.telemetry.basic import increment_metric
from cgc.utils.config_utils import get_namespace
from cgc.utils.message_utils import prepare_error_message
from cgc.utils.prepare_headers import get_api_url_and_prepare_headers
from cgc.utils.response_utils import response_precheck
from cgc.utils.click_group import CustomGroup, CustomCommand
from cgc.utils.consts.message_consts import TIMEOUT_ERROR, UNEXPECTED_ERROR


@click.group("billing", cls=CustomGroup)
def billing_group():
    """
    Access and manage billing information.
    """
    pass


@billing_group.command("status", cls=CustomCommand)
def billing_status():
    """
    Shows billing status for user namespace
    """
    metric_ok = f"{get_namespace()}.billing.status.ok"
    metric_error = f"{get_namespace()}.billing.status.error"

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/billing/status"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(response, metric_error)

        if response.status_code != 200:
            increment_metric(metric_error)
            message = "Error occuerd while getting billing status. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        total_cost = data["details"]["cost_total"]
        namespace = data["details"]["namespace"]
        user_list = data["details"]["details"]
        if not user_list:
            click.echo("No costs found")
            return

        print_billing_status(user_list)
        click.echo(f"Total cost for namespace {namespace}: {total_cost:.2f} pln\n")
        increment_metric(metric_ok)
    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@billing_group.command("invoice", cls=CustomCommand)
@click.option("--year", "-y", "year", prompt=True, type=int)
@click.option("--month", "-m", "month", prompt=True, type=click.IntRange(1, 12))
def billing_invoice(year: int, month: int):
    """
    Opens invoice from given year and month
    """
    metric_ok = f"{get_namespace()}.billing.invoice.ok"
    metric_error = f"{get_namespace()}.billing.invoice.error"

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/billing/invoice?year={year}&month={month}"
    try:
        response = requests.post(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(response, metric_error)

        if response.status_code != 200:
            click.echo(f"Error {response.status_code} {response.text}")
            increment_metric(metric_error)
            message = "Error occuerd while getting invoice status. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        total_cost = data["details"]["cost_total"]
        namespace = data["details"]["namespace"]
        user_list = data["details"]["invoice"]
        if not user_list:
            click.echo(f"No costs found for {calendar.month_name[month]} {year}")
            return

        print_billing_status(user_list)
        click.echo(
            f"Total cost for namespace {namespace} in {calendar.month_name[month]} {year}: {total_cost:.2f} pln\n"
        )
        increment_metric(metric_ok)

    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@click.group("stop_events", cls=CustomGroup)
def stop_events_group():
    """
    List stop events information.
    """
    pass


@stop_events_group.command("compute")
@click.option("--date_from", "-f", "date_from", prompt="Date from (DD-MM-YYYY)")
@click.option("--date_to", "-t", "date_to", prompt="Date to (DD-MM-YYYY)")
def stop_events_compute(date_from, date_to):
    try:
        datetime.datetime.strptime(date_from, "%d-%m-%Y")
        datetime.datetime.strptime(date_to, "%d-%m-%Y")
    except ValueError:
        click.echo("Incorrect date format, should be DD-MM-YYYY")
        return

    metric_ok = f"{get_namespace()}.billing.stop_events.compute.ok"
    metric_error = f"{get_namespace()}.billing.stop_events.compute.error"

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/billing/list_compute_stop_events?time_from={date_from}&time_till={date_to}"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(response, metric_error)

        if response.status_code != 200:
            click.echo(f"Error {response.status_code} {response.text}")
            increment_metric(metric_error)
            message = "Error occuerd while listing compute stop events. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        event_list = data["details"]["event_list"]
        if not event_list:
            click.echo("No compute stop events to list.")
            return
        click.echo("Compute stop events:")
        print_compute_stop_events(event_list)
        increment_metric(metric_ok)
    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


@stop_events_group.command("volume")
@click.option("--date_from", "-f", "date_from", prompt=True)
@click.option("--date_to", "-t", "date_to", prompt=True)
def stop_events_volume(date_from, date_to):
    try:
        datetime.datetime.strptime(date_from, "%d-%m-%Y")
        datetime.datetime.strptime(date_to, "%d-%m-%Y")
    except ValueError:
        click.echo("Incorrect date format, should be DD-MM-YYYY")
        return

    metric_ok = f"{get_namespace()}.billing.stop_events.volume.ok"
    metric_error = f"{get_namespace()}.billing.stop_events.volume.error"

    api_url, headers = get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/billing/list_storage_stop_events?time_from={date_from}&time_till={date_to}"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response_precheck(response, metric_error)

        if response.status_code != 200:
            click.echo(f"Error {response.status_code} {response.text}")
            increment_metric(metric_error)
            message = "Error occuerd while listing volume stop events. Try again or contact us at support@comtegra.pl"
            click.echo(prepare_error_message(message))
            return

        data = response.json()
        event_list = data["details"]["event_list"]
        if not event_list:
            click.echo("No volume stop events to list.")
            return
        click.echo("Volume stop events:")
        print_volume_stop_events(event_list)
        increment_metric(metric_ok)
    except KeyError:
        increment_metric(metric_error)
        click.echo(prepare_error_message(UNEXPECTED_ERROR))
    except requests.exceptions.ReadTimeout:
        increment_metric(metric_error)
        click.echo(prepare_error_message(TIMEOUT_ERROR))


billing_group.add_command(stop_events_group)
