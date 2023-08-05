# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_rpm.api_client import ApiClient
from pulpcore.client.pulp_rpm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContentPackagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, **kwargs):  # noqa: E501
        """Create a package  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact: Artifact file representing the physical content
        :param str relative_path: Path where the artifact is located relative to distributions base_path
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param str upload: An uncommitted upload that may be turned into the artifact of the content unit.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(**kwargs)  # noqa: E501

    def create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a package  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact: Artifact file representing the physical content
        :param str relative_path: Path where the artifact is located relative to distributions base_path
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param str upload: An uncommitted upload that may be turned into the artifact of the content unit.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'artifact',
            'relative_path',
            'file',
            'repository',
            'upload'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('relative_path' in local_var_params and  # noqa: E501
                                                        len(local_var_params['relative_path']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `relative_path` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'artifact' in local_var_params:
            form_params.append(('artifact', local_var_params['artifact']))  # noqa: E501
        if 'relative_path' in local_var_params:
            form_params.append(('relative_path', local_var_params['relative_path']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'repository' in local_var_params:
            form_params.append(('repository', local_var_params['repository']))  # noqa: E501
        if 'upload' in local_var_params:
            form_params.append(('upload', local_var_params['upload']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/packages/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List packages  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str arch: Filter results where arch matches value
        :param list[str] arch__in: Filter results where arch is in a comma-separated list of values
        :param str arch__ne: Filter results where arch not equal to value
        :param str checksum_type: Filter results where checksum_type matches value
        :param list[str] checksum_type__in: Filter results where checksum_type is in a comma-separated list of values
        :param str checksum_type__ne: Filter results where checksum_type not equal to value
        :param str epoch: Filter results where epoch matches value
        :param list[str] epoch__in: Filter results where epoch is in a comma-separated list of values
        :param str epoch__ne: Filter results where epoch not equal to value
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param str name__ne: Filter results where name not equal to value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering
        :param str pkg_id: Filter results where pkgId matches value
        :param list[str] pkg_id__in: Filter results where pkgId is in a comma-separated list of values
        :param str release: Filter results where release matches value
        :param list[str] release__in: Filter results where release is in a comma-separated list of values
        :param str release__ne: Filter results where release not equal to value
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str sha256:
        :param str version: Filter results where version matches value
        :param list[str] version__in: Filter results where version is in a comma-separated list of values
        :param str version__ne: Filter results where version not equal to value
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedrpmPackageResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(**kwargs)  # noqa: E501

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List packages  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str arch: Filter results where arch matches value
        :param list[str] arch__in: Filter results where arch is in a comma-separated list of values
        :param str arch__ne: Filter results where arch not equal to value
        :param str checksum_type: Filter results where checksum_type matches value
        :param list[str] checksum_type__in: Filter results where checksum_type is in a comma-separated list of values
        :param str checksum_type__ne: Filter results where checksum_type not equal to value
        :param str epoch: Filter results where epoch matches value
        :param list[str] epoch__in: Filter results where epoch is in a comma-separated list of values
        :param str epoch__ne: Filter results where epoch not equal to value
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param str name__ne: Filter results where name not equal to value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering
        :param str pkg_id: Filter results where pkgId matches value
        :param list[str] pkg_id__in: Filter results where pkgId is in a comma-separated list of values
        :param str release: Filter results where release matches value
        :param list[str] release__in: Filter results where release is in a comma-separated list of values
        :param str release__ne: Filter results where release not equal to value
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str sha256:
        :param str version: Filter results where version matches value
        :param list[str] version__in: Filter results where version is in a comma-separated list of values
        :param str version__ne: Filter results where version not equal to value
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedrpmPackageResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'arch',
            'arch__in',
            'arch__ne',
            'checksum_type',
            'checksum_type__in',
            'checksum_type__ne',
            'epoch',
            'epoch__in',
            'epoch__ne',
            'limit',
            'name',
            'name__in',
            'name__ne',
            'offset',
            'ordering',
            'pkg_id',
            'pkg_id__in',
            'release',
            'release__in',
            'release__ne',
            'repository_version',
            'repository_version_added',
            'repository_version_removed',
            'sha256',
            'version',
            'version__in',
            'version__ne',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'arch' in local_var_params and local_var_params['arch'] is not None:  # noqa: E501
            query_params.append(('arch', local_var_params['arch']))  # noqa: E501
        if 'arch__in' in local_var_params and local_var_params['arch__in'] is not None:  # noqa: E501
            query_params.append(('arch__in', local_var_params['arch__in']))  # noqa: E501
            collection_formats['arch__in'] = 'csv'  # noqa: E501
        if 'arch__ne' in local_var_params and local_var_params['arch__ne'] is not None:  # noqa: E501
            query_params.append(('arch__ne', local_var_params['arch__ne']))  # noqa: E501
        if 'checksum_type' in local_var_params and local_var_params['checksum_type'] is not None:  # noqa: E501
            query_params.append(('checksum_type', local_var_params['checksum_type']))  # noqa: E501
        if 'checksum_type__in' in local_var_params and local_var_params['checksum_type__in'] is not None:  # noqa: E501
            query_params.append(('checksum_type__in', local_var_params['checksum_type__in']))  # noqa: E501
            collection_formats['checksum_type__in'] = 'csv'  # noqa: E501
        if 'checksum_type__ne' in local_var_params and local_var_params['checksum_type__ne'] is not None:  # noqa: E501
            query_params.append(('checksum_type__ne', local_var_params['checksum_type__ne']))  # noqa: E501
        if 'epoch' in local_var_params and local_var_params['epoch'] is not None:  # noqa: E501
            query_params.append(('epoch', local_var_params['epoch']))  # noqa: E501
        if 'epoch__in' in local_var_params and local_var_params['epoch__in'] is not None:  # noqa: E501
            query_params.append(('epoch__in', local_var_params['epoch__in']))  # noqa: E501
            collection_formats['epoch__in'] = 'csv'  # noqa: E501
        if 'epoch__ne' in local_var_params and local_var_params['epoch__ne'] is not None:  # noqa: E501
            query_params.append(('epoch__ne', local_var_params['epoch__ne']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__in' in local_var_params and local_var_params['name__in'] is not None:  # noqa: E501
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
            collection_formats['name__in'] = 'csv'  # noqa: E501
        if 'name__ne' in local_var_params and local_var_params['name__ne'] is not None:  # noqa: E501
            query_params.append(('name__ne', local_var_params['name__ne']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
            collection_formats['ordering'] = 'csv'  # noqa: E501
        if 'pkg_id' in local_var_params and local_var_params['pkg_id'] is not None:  # noqa: E501
            query_params.append(('pkgId', local_var_params['pkg_id']))  # noqa: E501
        if 'pkg_id__in' in local_var_params and local_var_params['pkg_id__in'] is not None:  # noqa: E501
            query_params.append(('pkgId__in', local_var_params['pkg_id__in']))  # noqa: E501
            collection_formats['pkgId__in'] = 'csv'  # noqa: E501
        if 'release' in local_var_params and local_var_params['release'] is not None:  # noqa: E501
            query_params.append(('release', local_var_params['release']))  # noqa: E501
        if 'release__in' in local_var_params and local_var_params['release__in'] is not None:  # noqa: E501
            query_params.append(('release__in', local_var_params['release__in']))  # noqa: E501
            collection_formats['release__in'] = 'csv'  # noqa: E501
        if 'release__ne' in local_var_params and local_var_params['release__ne'] is not None:  # noqa: E501
            query_params.append(('release__ne', local_var_params['release__ne']))  # noqa: E501
        if 'repository_version' in local_var_params and local_var_params['repository_version'] is not None:  # noqa: E501
            query_params.append(('repository_version', local_var_params['repository_version']))  # noqa: E501
        if 'repository_version_added' in local_var_params and local_var_params['repository_version_added'] is not None:  # noqa: E501
            query_params.append(('repository_version_added', local_var_params['repository_version_added']))  # noqa: E501
        if 'repository_version_removed' in local_var_params and local_var_params['repository_version_removed'] is not None:  # noqa: E501
            query_params.append(('repository_version_removed', local_var_params['repository_version_removed']))  # noqa: E501
        if 'sha256' in local_var_params and local_var_params['sha256'] is not None:  # noqa: E501
            query_params.append(('sha256', local_var_params['sha256']))  # noqa: E501
        if 'version' in local_var_params and local_var_params['version'] is not None:  # noqa: E501
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'version__in' in local_var_params and local_var_params['version__in'] is not None:  # noqa: E501
            query_params.append(('version__in', local_var_params['version__in']))  # noqa: E501
            collection_formats['version__in'] = 'csv'  # noqa: E501
        if 'version__ne' in local_var_params and local_var_params['version__ne'] is not None:  # noqa: E501
            query_params.append(('version__ne', local_var_params['version__ne']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/packages/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedrpmPackageResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, rpm_package_href, **kwargs):  # noqa: E501
        """Inspect a package  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(rpm_package_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_package_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RpmPackageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(rpm_package_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, rpm_package_href, **kwargs):  # noqa: E501
        """Inspect a package  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(rpm_package_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_package_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RpmPackageResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_package_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_package_href' is set
        if self.api_client.client_side_validation and ('rpm_package_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_package_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_package_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_package_href' in local_var_params:
            path_params['rpm_package_href'] = local_var_params['rpm_package_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_package_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RpmPackageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
